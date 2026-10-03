from urllib import response
import bcrypt
from src.database.config import supabase
from typing import Any, Dict, cast

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()

def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(),hashed.encode())

def check_teacher_exists(username):
    # Returns True if username exists, False if available
    response = (
        supabase.table("teachers")
        .select("username")
        .eq("username", username)
        .execute()
    )
    return len(response.data) > 0


def create_teacher(username, password, name):
    # Guard check: stop if username already exists
    if check_teacher_exists(username):
        return {"error": "Username already taken"}

    data = {
        "username": username,
        "password": hash_pass(password),
        "name": name,
    }

    response = supabase.table("teachers").insert(data).execute()
    return response 


def teacher_login(username, password):
    
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = cast(Dict[str, Any], response.data[0])
        if check_pass(password, teacher['password']):
            return teacher
    return None 

def get_all_images():
    response = supabase.table("students").select('*').execute()
    return response.data 

def create_student(new_name, face_embedding=None, voice_embedding=None):

    data = {
        "name": new_name,
        "face_embedding": face_embedding,
        "audio_embedding": voice_embedding
    }
    response = supabase.table("students").insert(data).execute()
    return response.data 


def create_subject(subject_code, name, section, teacher_id):
    data = {"subject_code": subject_code, "name": name, "section": section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data 


def get_teacher_subjects(teacher_id): 

    response = supabase.table('subjects').select("*, subject_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = response.data

    for sub in subjects:
        sub['total_students'] = sub.get("subject_students", [{}])[0].get('count', 0) if sub.get('subject_students') else 0 #type: ignore
        attendance = sub.get('attendance_logs', []) #type: ignore
        unique_sessions = len(set(log['timestamp'] for log in attendance))#type: ignore
        sub['total_classes'] = unique_sessions #type: ignore


        sub.pop('subject_student', None) #type: ignore
        sub.pop('attendance_logs', None) #type: ignore

    return subjects 


def enroll_student_to_subject(student_id, subject_id):
    try:
        data = {
            "student_id": student_id,
            "subject_id": subject_id
        }

        response = (
            supabase
            .table("subject_students")
            .insert(data)
            .execute()
        )

        return response.data

    except Exception as e:
        print(f"Enrollment error: {e}")
        return None


def  unenroll_student_to_subject(student_id, subject_id): 
    response= supabase.table('subject_students').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data 



def get_student_subjects(student_id):
    response = supabase.table('subject_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teacher_id): 
    response = supabase.table('attendance_logs').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data 


