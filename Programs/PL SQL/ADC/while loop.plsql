DECLARE
Counter NUMBER:=1;

BEGIN
WHILE Counter <=5 LOOP
DBMS_OUTPUT.PUT_LINE('Counter is ' ||Counter);

Counter:=Counter+1;
END LOOP;

DBMS_OUTPUT.PUT_LINE('END of While_loop.');
END;