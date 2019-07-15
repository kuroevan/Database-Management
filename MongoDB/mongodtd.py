from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.University

try:

    db.advisor.insert( [
        { 's_ID': '12345', 'i_ID': '10101'},
        { 's_ID': '00128', 'i_ID': '45565'},
        { 's_ID': '23121', 'i_ID': '76543'},
        { 's_ID': '44553', 'i_ID': '22222'},
        { 's_ID': '76543', 'i_ID': '45565'},
        { 's_ID': '98765', 'i_ID': '98345'},
        { 's_ID': '98988', 'i_ID': '76766'}
    ] )

    db.classroom.insert( [
        { 'building': 'Packard', 'room_number': '101', 'capacity': '500' },
        { 'building': 'Painter', 'room_number': '514', 'capacity': '10' },
        { 'building': 'Taylor', 'room_number': '3128', 'capacity': '70' },
        { 'building': 'Watson', 'room_number': '120', 'capacity': '50' }
    ] )

    db.course.insert( [
        { 'course_id': 'BIO-101', 'title': 'Intro to Biology', 'dept_name': 'Biology', 'credits': '4'  },
        { 'course_id': 'BIO-301', 'title': 'Genetics', 'dept_name': 'Biology', 'credits': '4'  },
        { 'course_id': 'BIO-399', 'title': 'Computational Biology', 'dept_name': 'Biology', 'credits': '3'  },
        { 'course_id': 'CS-101', 'title': 'Intro to Computer Science', 'dept_name': 'Comp. Sci.', 'credits': '4'  },
        { 'course_id': 'CS-190', 'title': 'Game Design', 'dept_name': 'Comp. Sci.', 'credits': '4'  },
        { 'course_id': 'CS-315', 'title': 'Robotics', 'dept_name': 'Comp. Sci.', 'credits': '3'  },
        { 'course_id': 'CS-319', 'title': 'Image Processing', 'dept_name': 'Comp. Sci.', 'credits': '3'  },
        { 'course_id': 'CS-347', 'title': 'Database System Concepts', 'dept_name': 'Comp. Sci.', 'credits': '3'  },
        { 'course_id': 'EE-101', 'title': 'Intro to Digital Systems', 'dept_name': 'Elec. Eng.', 'credits': '3'  },
        { 'course_id': 'FIN-201', 'title': 'Investment Banking', 'dept_name': 'Finance', 'credits': '3'  },
        { 'course_id': 'HIS-351', 'title': 'World History', 'dept_name': 'History', 'credits': '3'  },
        { 'course_id': 'PHY-101', 'title': 'Physical Principles', 'dept_name': 'Physics', 'credits': '4'  }
    ] )


    db.department.insert( [
        { 'dept_name': 'Biology', 'building': 'Watson', 'budget': '90000' },
        { 'dept_name': 'Comp. Sci.', 'building': 'Taylor', 'budget': '100000' },
        { 'dept_name': 'Elec. Eng.', 'building': 'Taylor', 'budget': '85000' },
        { 'dept_name': 'Finance', 'building': 'Painter', 'budget': '120000' },
        { 'dept_name': 'History', 'building': 'Painter', 'budget': '50000' },
        { 'dept_name': 'Music', 'building': 'Packard', 'budget': '80000' },
        { 'dept_name': 'Physics', 'building': 'Watson', 'budget': '70000' }
    ] )

    db.instructor.insert( [
        { 'id': '10101', 'name': 'Srinivasan', 'dept_name': 'Comp. Sci.', 'salary': '65000' },
        { 'id': '12121', 'name': 'Wu', 'dept_name': 'Finance', 'salary': '90000' },
        { 'id': '15151', 'name': 'Mozart', 'dept_name': 'Music', 'salary': '40000' },
        { 'id': '22222', 'name': 'Einstein', 'dept_name': 'Physics', 'salary': '95000' },
        { 'id': '32343', 'name': 'El Said', 'dept_name': 'History', 'salary': '60000' },
        { 'id': '33456', 'name': 'Gold', 'dept_name': 'Physics', 'salary': '87000' },
        { 'id': '45565', 'name': 'Katz', 'dept_name': 'Comp. Sci.', 'salary': '75000' },
        { 'id': '58583', 'name': 'Califeri', 'dept_name': 'History', 'salary': '62000' },
        { 'id': '76543', 'name': 'Singh', 'dept_name': 'Finance', 'salary': '80000' },
        { 'id': '76766', 'name': 'Crick', 'dept_name': 'Biology', 'salary': '72000' },
        { 'id': '83821', 'name': 'Brandt', 'dept_name': 'Comp. Sci.', 'salary': '92000' },
        { 'id': '98345', 'name': 'Kim', 'dept_name': 'Elec. Eng.', 'salary': '80000' }
    ] )

    db.prereq.insert( [
        { 'course_id': 'BIO-301', 'prereq_id': 'BIO-101' },
        { 'course_id': 'BIO-399', 'prereq_id': 'BIO-101' },
        { 'course_id': 'CS-190', 'prereq_id': 'CS-101' },
        { 'course_id': 'CS-315', 'prereq_id': 'CS-101' },
        { 'course_id': 'CS-319', 'prereq_id': 'CS-101' },
        { 'course_id': 'CS-347', 'prereq_id': 'CS-101' },
        { 'course_id': 'EE-181', 'prereq_id': 'PHY-101' }
    ] )

    db.section.insert( [
        { 'course_id': 'BIO-101', 'sec_id': '1', 'semester': 'Summer', 'year': '2009', 'building': 'Painter', 'room_number': '514', 'time_slot_id': 'B' },
        { 'course_id': 'BIO-301', 'sec_id': '1', 'semester': 'Summer', 'year': '2010', 'building': 'Painter', 'room_number': '514', 'time_slot_id': 'A' },
        { 'course_id': 'CS-101', 'sec_id': '1', 'semester': 'Fall', 'year': '2009', 'building': 'Packard', 'room_number': '101', 'time_slot_id': 'H' },
        { 'course_id': 'CS-101', 'sec_id': '1', 'semester': 'Spring', 'year': '2010', 'building': 'Packard', 'room_number': '101', 'time_slot_id': 'F' },
        { 'course_id': 'CS-190', 'sec_id': '2', 'semester': 'Spring', 'year': '2009', 'building': 'Taylor', 'room_number': '3128', 'time_slot_id': 'E' },
        { 'course_id': 'CS-190', 'sec_id': '2', 'semester': 'Spring', 'year': '2009', 'building': 'Taylor', 'room_number': '3128', 'time_slot_id': 'A' },
        { 'course_id': 'CS-315', 'sec_id': '1', 'semester': 'Spring', 'year': '2010', 'building': 'Watson', 'room_number': '120', 'time_slot_id': 'D' },
        { 'course_id': 'CS-319', 'sec_id': '1', 'semester': 'Spring', 'year': '2010', 'building': 'Watson', 'room_number': '100', 'time_slot_id': 'B' },
        { 'course_id': 'CS-347', 'sec_id': '1', 'semester': 'Fall', 'year': '2009', 'building': 'Taylor', 'room_number': '3128', 'time_slot_id': 'A' },
        { 'course_id': 'EE-181', 'sec_id': '1', 'semester': 'Spring', 'year': '2009', 'building': 'Taylor', 'room_number': '3128', 'time_slot_id': 'C' },
        { 'course_id': 'FIN-201', 'sec_id': '1', 'semester': 'Spring', 'year': '2010', 'building': 'Packard', 'room_number': '101', 'time_slot_id': 'B' },
        { 'course_id': 'HIS-351', 'sec_id': '1', 'semester': 'Spring', 'year': '2010', 'building': 'Painter', 'room_number': '514', 'time_slot_id': 'C' },
        { 'course_id': 'MU-199', 'sec_id': '1', 'semester': 'Spring', 'year': '2010', 'building': 'Packard', 'room_number': '101', 'time_slot_id': 'D' },
        { 'course_id': 'PHY-101', 'sec_id': '1', 'semester': 'Fall', 'year': '2009', 'building': 'Watson', 'room_number': '100', 'time_slot_id': 'A' }
    ]  )

    db.student.insert( [
        { 'id': '00128', 'name': 'Zhang', 'dept_name': 'Comp. Sci.', 'tot_cred': '102' },
        { 'id': '12345', 'name': 'Shankar', 'dept_name': 'Comp. Sci.', 'tot_cred': '32' },
        { 'id': '19991', 'name': 'Brandt', 'dept_name': 'History', 'tot_cred': '80' },
        { 'id': '23121', 'name': 'Chavez', 'dept_name': 'Finance', 'tot_cred': '110' },
        { 'id': '44553', 'name': 'Peltier', 'dept_name': 'Physics', 'tot_cred': '56' },
        { 'id': '45678', 'name': 'Levy', 'dept_name': 'Physics', 'tot_cred': '46' },
        { 'id': '54321', 'name': 'Williams', 'dept_name': 'Comp. Sci.', 'tot_cred': '54' },
        { 'id': '55739', 'name': 'Sanchez', 'dept_name': 'Music', 'tot_cred': '38' },
        { 'id': '70557', 'name': 'Snow', 'dept_name': 'Physics', 'tot_cred': '0' },
        { 'id': '76543', 'name': 'Brown', 'dept_name': 'Comp. Sci.', 'tot_cred': '58' },
        { 'id': '76653', 'name': 'Aoi', 'dept_name': 'Elec. Eng.', 'tot_cred': '60' },
        { 'id': '98765', 'name': 'Bourikas', 'dept_name': 'Elec. Eng.', 'tot_cred': '98' },
        { 'id': '98988', 'name': 'Tanaka', 'dept_name': 'Biology', 'tot_cred': '120' }
    ] )

    db.teaches.insert( [
        { 'id': '75766', 'course_id': 'BIO-101', 'sec_id': '1', 'semester': 'Summer', 'year': '2009' },
        { 'id': '75766', 'course_id': 'BIO-301', 'sec_id': '1', 'semester': 'Summer', 'year': '2010' },
        { 'id': '10101', 'course_id': 'CS-101', 'sec_id': '1', 'semester': 'Fall', 'year': '2009' },
        { 'id': '45565', 'course_id': 'CS-101', 'sec_id': '1', 'semester': 'Spring', 'year': '2010' },
        { 'id': '83821', 'course_id': 'CS-190', 'sec_id': '1', 'semester': 'Spring', 'year': '2009' },
        { 'id': '83821', 'course_id': 'CS-190', 'sec_id': '2', 'semester': 'Spring', 'year': '2009' },
        { 'id': '10101', 'course_id': 'CS-315', 'sec_id': '1', 'semester': 'Spring', 'year': '2010' },
        { 'id': '45565', 'course_id': 'CS-319', 'sec_id': '1', 'semester': 'Spring', 'year': '2010' },
        { 'id': '83821', 'course_id': 'CS-319', 'sec_id': '2', 'semester': 'Spring', 'year': '2010' },
        { 'id': '10101', 'course_id': 'CS-347', 'sec_id': '1', 'semester': 'Fall', 'year': '2009' },
        { 'id': '98345', 'course_id': 'EE-181', 'sec_id': '1', 'semester': 'Spring', 'year': '2009' },
        { 'id': '12121', 'course_id': 'FIN-201', 'sec_id': '1', 'semester': 'Spring', 'year': '2010' },
        { 'id': '32343', 'course_id': 'HIS-351', 'sec_id': '1', 'semester': 'Spring', 'year': '2010' },
        { 'id': '15151', 'course_id': 'MU-199', 'sec_id': '1', 'semester': 'Spring', 'year': '2010' },
        { 'id': '22222', 'course_id': 'PHY-101', 'sec_id': '1', 'semester': 'Fall', 'year': '2009' }
    ] )

    db.takes.insert( [
        {'id': '00128','course_id': 'CS-101','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'A' },
        {'id': '00128','course_id': 'CS-347','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'A-' },
        {'id': '12345','course_id': 'CS-101','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'C' },
        {'id': '12345','course_id': 'CS-315','sec_id': '1','semester': 'Spring','year': '2010', 'grade': 'A' },
        {'id': '12345','course_id': 'CS-347','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'A' },
        {'id': '19991','course_id': 'HIS-351','sec_id': '1','semester': 'Spring','year': '2010', 'grade': 'B' },
        {'id': '23121','course_id': 'FIN-201','sec_id': '1','semester': 'Spring','year': '2010', 'grade': 'C+' },
        {'id': '44553','course_id': 'PHY-101','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'B-' },
        {'id': '45678','course_id': 'CS-101','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'F' },
        {'id': '45678','course_id': 'CS-101','sec_id': '1','semester': 'Spring','year': '2010', 'grade': 'B+' },
        {'id': '45678','course_id': 'CS-319','sec_id': '1','semester': 'Spring','year': '2010', 'grade': 'B' },
        {'id': '54321','course_id': 'CS-101','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'A-' },
        {'id': '54321','course_id': 'CS-190','sec_id': '2','semester': 'Spring','year': '2009', 'grade': 'B+' },
        {'id': '55739','course_id': 'MU-199','sec_id': '1','semester': 'Spring','year': '2010', 'grade': 'A-' },
        {'id': '76543','course_id': 'CS-101','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'A' },
        {'id': '76543','course_id': 'CS-319','sec_id': '2','semester': 'Spring','year': '2010', 'grade': 'A' },
        {'id': '76543','course_id': 'EE-181','sec_id': '1','semester': 'Spring','year': '2009', 'grade': 'C' },
        {'id': '98765','course_id': 'CS-101','sec_id': '1','semester': 'Fall','year': '2009', 'grade': 'C-' },
        {'id': '98765','course_id': 'CS-315','sec_id': '1','semester': 'Spring','year': '2010', 'grade': 'B' },
        {'id': '98988','course_id': 'BIO-101','sec_id': '1','semester': 'Summer','year': '2009', 'grade': 'A' },
        {'id': '98988','course_id': 'BIO-301','sec_id': '1','semester': 'Summer','year': '2010', 'grade': '-' }
    ] )

    db.time_slot.insert( [
        { 'time_slot_id': 'A', 'day': 'F', 'start_hr': '8', 'start_min': '0', 'end_hr': '8', 'end_min': '50' },
        { 'time_slot_id': 'A', 'day': 'M', 'start_hr': '8', 'start_min': '0', 'end_hr': '8', 'end_min': '50' },
        { 'time_slot_id': 'A', 'day': 'W', 'start_hr': '8', 'start_min': '0', 'end_hr': '8', 'end_min': '50' },
        { 'time_slot_id': 'B', 'day': 'F', 'start_hr': '9', 'start_min': '0', 'end_hr': '9', 'end_min': '50' },
        { 'time_slot_id': 'B', 'day': 'M', 'start_hr': '9', 'start_min': '0', 'end_hr': '9', 'end_min': '50' },
        { 'time_slot_id': 'B', 'day': 'W', 'start_hr': '9', 'start_min': '0', 'end_hr': '9', 'end_min': '50' },
        { 'time_slot_id': 'C', 'day': 'F', 'start_hr': '11', 'start_min': '0', 'end_hr': '11', 'end_min': '50' },
        { 'time_slot_id': 'C', 'day': 'M', 'start_hr': '11', 'start_min': '0', 'end_hr': '11', 'end_min': '50' },
        { 'time_slot_id': 'C', 'day': 'W', 'start_hr': '11', 'start_min': '0', 'end_hr': '11', 'end_min': '50' },
        { 'time_slot_id': 'D', 'day': 'F', 'start_hr': '13', 'start_min': '0', 'end_hr': '13', 'end_min': '50' },
        { 'time_slot_id': 'D', 'day': 'M', 'start_hr': '13', 'start_min': '0', 'end_hr': '13', 'end_min': '50' },
        { 'time_slot_id': 'D', 'day': 'W', 'start_hr': '13', 'start_min': '0', 'end_hr': '13', 'end_min': '50' },
        { 'time_slot_id': 'E', 'day': 'R', 'start_hr': '10', 'start_min': '30', 'end_hr': '11', 'end_min': '45' },
        { 'time_slot_id': 'E', 'day': 'T', 'start_hr': '10', 'start_min': '30', 'end_hr': '11', 'end_min': '45' },
        { 'time_slot_id': 'F', 'day': 'R', 'start_hr': '14', 'start_min': '30', 'end_hr': '15', 'end_min': '45' },
        { 'time_slot_id': 'F', 'day': 'T', 'start_hr': '14', 'start_min': '30', 'end_hr': '15', 'end_min': '45' },
        { 'time_slot_id': 'G', 'day': 'F', 'start_hr': '16', 'start_min': '0', 'end_hr': '16', 'end_min': '50' },
        { 'time_slot_id': 'G', 'day': 'M', 'start_hr': '16', 'start_min': '0', 'end_hr': '16', 'end_min': '50' },
        { 'time_slot_id': 'G', 'day': 'W', 'start_hr': '16', 'start_min': '0', 'end_hr': '16', 'end_min': '50' },
        { 'time_slot_id': 'H', 'day': 'W', 'start_hr': '10', 'start_min': '0', 'end_hr': '12', 'end_min': '30' }
    ] )

    print('Database creation success!')

except:
    print('Database creation failure!')
