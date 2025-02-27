' AIM: To find Addition/ Subtraction/ Multiplication/ Divison of two given numbers by using select case statement/

Private Sub Form_Click ()
	Dim a, b as Integer
	Dim choice As string
	a = InputBox("Enter First Number")
	b = InputBox("Enter Second Number")
	choice = InputBox("Enter your choice a/s/m/d")
	Select case choice
	Case "a", "A", "+"
	 Msgbox("Addition of enterd numbers is" &a+b)
 	Case "s", "S", "+"
	 Msgbox("Subtraction of enterd numbers is" &a-b)
 	Case "m", "M", "+"
	 Msgbox("Multiplication of enterd numbers is" &a*b)
  	Case "d", "D", "+"
	 Msgbox("Divison of enterd numbers is" &a/b)
  	Case Else
  	Msgbox("You Entred on invaild")
End Sub

Private Sub Form_Click ()
	Dim name As string
	name = InputBox("Enter your naem")
	Msgbox(nam&"Welcome to my project")
End Sub