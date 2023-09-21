def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    student_count = 0

    for student_entrance, student_exit in permanence_period:
        if isinstance(student_entrance, int) and isinstance(student_exit, int):
            if student_entrance <= target_time <= student_exit:
                student_count += 1

    return student_count
