DECLARE
    NUM_ITERATIONS NUMBER:=5;
    COUNTER NUMBER;
    TOTAL_SUM NUMBER:=0;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Starting the loop...');
    FOR COUNTER IN 1..NUM_ITERATIONS LOOP
        TOTAL_SUM:=TOTAL_SUM+COUNTER;
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('loop Completed.');
    DBMS_OUTPUT.PUT_LINE('Total sum is ' ||TOTAL_SUM);
END;