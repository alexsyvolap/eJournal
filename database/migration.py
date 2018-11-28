import sqlalchemy as sa
import helper as help


class Users(help.BaseModel):
    __tablename__ = 'users'
    __repr_attrs__ = ['id', 'fname', 'lname', 'sname', 'password', 'is_teacher']
    id = sa.Column(sa.String(25), primary_key=True)
    fname = sa.Column(sa.String(25))
    lname = sa.Column(sa.String(25))
    sname = sa.Column(sa.String(25))
    password = sa.Column(sa.String(25))
    is_teacher = sa.Column(sa.SmallInteger)

    @staticmethod
    def _bootstrap(student=500, teacher=150, locale='uk'):
        from mimesis import Person

        person = Person(locale)

        for _ in range(student):
            user = Users(
                id=student,
                fname=person.name(),
                lname=person.last_name(),
                sname=person.surname(),
                password=student,
                is_teacher=0
            )

            help.session.add(user)
            try:
                help.session.commit()
                print(student)
            except Exception:
                help.session.rollback()

        for _ in range(teacher):
            username = person.username()
            user = Users(
                id=username,
                fname=person.name(),
                lname=person.last_name(),
                sname=person.surname(),
                password=username,
                is_teacher=1
            )

            help.session.add(user)
            try:
                help.session.commit()
                print(teacher)
            except Exception:
                help.session.rollback()
