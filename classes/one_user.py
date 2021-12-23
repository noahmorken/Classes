from users import Admin

a_user = Admin('Wholesome', 'One Hundred', 10, 'F')
print("\n")
a_user.describe_user()
a_user.greet_user()
a_user.increment_login_attempts()
a_user.increment_login_attempts()
a_user.increment_login_attempts()
a_user.increment_login_attempts()
a_user.increment_login_attempts()
a_user.reset_login_attempts()
a_user.privileges.show_privileges()