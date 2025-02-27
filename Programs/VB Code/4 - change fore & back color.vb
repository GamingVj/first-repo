' AIM: Change of Forecolor (text colour) and Backcolor (Background colour) of text box and object by using option button control.

Private Sub OPTBLACK_Click ()
	LBLONE.Backcolor = vbBlack
	TXTONE.Backcolor = vbBlack
End Sub

Private Sub OPTCYAN_Click ()
	LBLONE.Backcolor = vbCyan
	TXTONE.Backcolor = vbCyan
End Sub

Private Sub OPTMAGENTA_Click ()
	LBLONE.Backcolor = vbMagenta
	TXTONE.Backcolor = vbMagenta
End Sub

Private Sub OPTRED_Click ()
	LBLONE.Forecolor = vbRed
	TXTONE.Forecolor = vbRed
End Sub

Private Sub OPTGREEN_Click ()
	LBLONE.Forecolor = vbGreen
	TXTONE.Forecolor = vbGreen
End Sub

Private Sub OPTYELLOW_Click ()
	LBLONE.Forecolor = vbYellow
	TXTONE.Forecolor = vbYellow
End Sub

