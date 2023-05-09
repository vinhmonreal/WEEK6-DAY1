from flask import render_template

from . import bp


@bp.route('/car1')
def car1():
    return render_template('car1.jinja', title = 'Car 1')
@bp.route('/car2')
def car2():
    return render_template('car2.jinja', title = 'Car 2')
@bp.route('/car3')
def car3():
    return render_template('car3.jinja', title = 'Car 3')


