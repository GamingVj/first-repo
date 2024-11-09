Create or replace type my_nested_table is table of VARCHAR2(10);

Create table my_subject(sub_id number, sub_name VARCHAR2(20), sub_schedule_day, my_nested_table)
nested table sub_schedule_day store as nested_tabspace;

desc my_subject;

insert into my_subject(sub_id, sub_name, sub_schedule_day) values(101, 'maths', my_nested_table('Mon', 'Fri'));
insert into my_subject(sub_id, sub_name, sub_schedule_day) values(102, 'Sci', my_nested_table('Mon', 'Tue', 'Fri'));
insert into my_subject(sub_id, sub_name, sub_schedule_day) values(103, 'Hist', my_nested_table('Mon', 'Tue', 'Wed', 'Fri'));
insert into my_subject(sub_id, sub_name, sub_schedule_day) values(104, 'Geo', my_nested_table('Mon', 'Tue', 'Wed', 'Fri', 'Sat'));
insert into my_subject(sub_id, sub_name, sub_schedule_day) values(105, 'CS', my_nested_table('Mon', 'Tue', 'Fri', 'Sat'));

Select * FROM my_subject;