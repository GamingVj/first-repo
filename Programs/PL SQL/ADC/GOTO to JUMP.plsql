DECLARE
    V_COUNTER NUMBER:=1;
BEGIN
    LOOP
        IF V_COUNTER>10 THEN
            GOTO EXIT_LOOP;
        END IF;

        DBMS_OUTPUT.PUT_LINE('Counter is '
                             ||V_COUNTER);
        V_COUNTER:=V_COUNTER+1;
        IF V_COUNTER=5 THEN
            NULL;
        END IF;
    END LOOP;

    <<EXIT_LOOP>>
    DBMS_OUTPUT.PUT_LINE('END of Loop.');
END;
/