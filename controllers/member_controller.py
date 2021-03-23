from flask import Blueprint, Flask, redirect, render_template, request
from models.member import Member
import repositories.member_repository as member_repository
import datetime

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template('members/index.html', members=members)

@members_blueprint.route('/members/<id>')
def member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)

@members_blueprint.route('/members/<id>', methods=['POST'])
def edit_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    email = request.form['email']
    phone = request.form['phone']
    if request.form.get('membership'):
        membership = True
        member_since = request.form['member_since']
        member_until = request.form['member_until']
        if request.form.get('premium'):
            premium = True
        else:
            premium = False
    else:
        membership = False
        premium = False
        member_since = None
        member_until = None
    member = Member(first_name, last_name, email, phone, date_of_birth, membership,
                    premium, member_since, member_until, id)
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route('/members/new')
def new_member():
    return render_template('members/new.html')

@members_blueprint.route('/members/new', methods=['POST'])
def add_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    email = request.form['email']
    phone = request.form['phone']
    if request.form.get('membership'):
        membership = True
        member_since = request.form['member_since']
        member_until = request.form['member_until']
        if request.form.get('premium'):
            premium = True
        else:
            premium = False
    else:
        membership = False
        premium = False
        member_since = None
        member_until = None
    member = Member(first_name, last_name, email, phone, date_of_birth, membership,
                    premium, member_since, member_until, id)
    member_repository.save(member)
    return redirect('/members')

@members_blueprint.route('/members/<id>/delete', methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')