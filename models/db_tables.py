import datetime


db.define_table('courses',
	Field('codeCourese', 'string', required=True, notnull=True),
	Field('name', 'string'),
	Field('description', 'string'),
	Field('prerequisites', 'string', 'reference courses',
		requires=IS_IN_DB(db, 'courses.codeCourese', '%(name)s'),notnull=False),
	Field('instructor', 'string'),
	Field('capacity', 'integer'),
	Field('scheduleId', 'integer', 
		'reference coursessechedules', 
		requires=IS_IN_DB(db, 'coursessechedules.id', '%(days)s: %(startTime)s - %(endTime)s'),unique=True),
	primarykey=['codeCourese']
	)
db.define_table('rooms',
	Field('code', 'string', required=True, notnull=True),
	primarykey=['code'])

db.define_table('coursessechedules',
	Field('id', 'integer'),
	Field('days', 'string'),
	Field('startTime', 'time', default=datetime.time(0,0)),
	Field('endTime', 'time', default=datetime.time(0,0)),
	Field('roomNo', 'string', 'reference rooms', requires=IS_IN_DB(db,'rooms.code', '%(code)s') )
	)