from django.shortcuts import render, redirect


def problem_list(req):
    return render(req, 'Admin_Problem_Show.html')