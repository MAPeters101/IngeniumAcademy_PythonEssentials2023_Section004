def format_info(age, name, job):
    formatted_info = {
        'age': age,
        'name': name,
        'job': job,
        'description': f"{name} is a {age} year old {job}."
    }
    return formatted_info

if __name__ == '__main__':
    age, name, job =  30, 'John', 'Software Developer'

    formatted_data = format_info(age=age, name=name, job=job)
    print(formatted_data)

    #formatted_data = format_info(age=age, name=name, job)  # This will fail because keyword argument before non-keyword argument
    #print(formatted_data)

    formatted_data = format_info(age, name=name, job=job)
    print(formatted_data)




