def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    for student_entrance, student_exit in permanence_period:
        if not isinstance(student_entrance, int) or not isinstance(student_exit, int):
            return None

    student = 0

    for student_entrance, student_exit in permanence_period:
        if student_entrance <= target_time <= student_exit:
            student += 1

    return student

    """Faça o código aqui."""
    raise NotImplementedError
