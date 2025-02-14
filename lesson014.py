def func_with_args_and_kwargs(*args, **kwargs):
    print(f"Arguments were: {args}")
    print(f"Type of args: {type(args)}")

    print(f"Keyword Arguments were: {kwargs}")
    print(f"Type of args: {type(kwargs)}")

def common_function(age, name, job, **kwargs):
    formatted_info = {
        'age': age,
        'name': name,
        'job': job,
        'description': f"{name} is a {age} year old {job}.",
        'additional_info': kwargs # NESTED DICTIONARY
    }
    return formatted_info

if __name__ == '__main__':

    age, name, job = 30, 'Jane', 'Software Developer'

    print(common_function(age, name, job, experience=10, company='Google'))

    print('-'*40)

    func_with_args_and_kwargs(1, 2, 3, a=4, b=5, c=6)


