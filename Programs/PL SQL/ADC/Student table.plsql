Create table start (id number primary key, name, VARCHAR2(10));

Create sequence roll_seq
    start with 1
    increment by 1
    max value 10
    no cycle;

insert into student values(roll_seq, nextvalue, 'prem');
insert into student values(roll_seq, nextvalue, 'prerana');
insert into student values(roll_seq, nextvalue, 'prashant');
insert into student values(roll_seq, nextvalue, 'prachi');
insert into student values(roll_seq, nextvalue, 'pramod');

SELECT * FROM student;

alter SEQUENCE roll_seq increment by 2;

insert into student values(roll_seq, nextvalue, 'pankaj');

drop SEQUENCE roll_seq;