from mazypages.models import User, Plan


def get_all_users():
    users = [
        user for user in User.objects.all()
    ]

    return users


def get_plan():
    plan = [
        plan for plan in Plan.objects.all()
    ]

    return plan
