# models.py
class College:
    def __init__(self,
                 id=None,
                 school_name=None,
                 student_size=None,
                 state=None,
                 tuition_in_state=None,
                 tuition_out_of_state=None,
                 latitude=None,
                 longitude=None,
                 school_type=None,
                 degree_length=None):
        self.id = id
        self.school_name = school_name
        self.student_size = student_size
        self.state = state
        self.tuition_in_state = tuition_in_state
        self.tuition_out_of_state = tuition_out_of_state
        self.latitude = latitude
        self.longitude = longitude
        self.school_type = school_type
        self.degree_length = degree_length

    def to_dict(self):
        return {
            'id': self.id,
            'school_name': self.school_name,
            'student_size': self.student_size,
            'state': self.state,
            'tuition_in_state': self.tuition_in_state,
            'tuition_out_of_state': self.tuition_out_of_state,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'school_type': self.school_type,
            'degree_length': self.degree_length,
        }
