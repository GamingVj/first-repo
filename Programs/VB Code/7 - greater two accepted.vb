' AIM: Write a program in Visual Basic to check which no. is greater among the two accepted numbers.

Private Sub Form_load ()
	Msgbox("Welcome to my Project" &Now)
End Sub

Private Sub Form_Click ()
	Dim a, b as Integer
	a = inputbox("Enter First number")
	b = inputbox("Enter Second number")
	If a>b Then
	Msgbox("First no. is greater than Second no.")
	Else if b>a Then
	Msgbox("Second no. is greater than First no.")
	Else if b>a Then
	Msgbox("Second no. is greater than first no.")
	Else
	Msgbox("Both the numbers are equal")
	End If
End Sub