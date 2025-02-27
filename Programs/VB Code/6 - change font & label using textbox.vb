' AIM: To change the Font Style of Text by using Textbox or Label object and check box content.

Private Sub CHKBOLD_Click ()
	If CHKBOLD.value = 1 Then
	LBLONE.FontBold = True
	Else
	LBLONE.FontBold = False
	End If
End Sub

Private Sub CHKITALIC_Click ()
	If CHKITALIC.value = 1 Then
	LBLONE.FontItalic = True
	Else
	LBLONE.FontItalic = False
	End If
End Sub

Private Sub CHKUNDERLINE_Click ()
	If CHKUNDERLINE.value = 1 Then
	LBLONE.FontUnderline = True
	Else
	LBLONE.FontUnderline = False
	End If
End Sub

Private Sub CHKSTRIKE_Click ()
	If CHKSTRIKE.value = 1 Then
	LBLONE.FontStrikethru = True
	Else
	LBLONE.FontStrikethru = False
	End If
End Sub

Private Sub CMDEXIT_Click ()
	End
End Sub