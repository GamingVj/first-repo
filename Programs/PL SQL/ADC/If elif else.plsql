DECLARE
    V_NUMBER INTERGER :- 15;
    V_RESULT VARCHAR(50);
BEGIN
    IF V_NUMBER < 10 THEN
        V_RESULT := 'Number is less than 10';
    ELSIF V_NUMBER>=10 AND V_NUMBER<20 THEN
        V_RESULT := 'Number is between 10 and 20';
    ELSE
        V_RESULT:='Number is between 10 and 19';
    ELSE
        V_RESULT := 'Number is greater than 20';
    END IF;

    DBMS_OUTPUT.PUT_LINE('IF...THEN...ELSE Example');
    DBMS_OUTPUT.PUT_LINE(V_RESULT);
END;