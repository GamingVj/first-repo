' AIM : Creation of Calculator Application by using label and textbox objects and commadn button control.

Private Sub CMDCLEAR_Click ()
	LBLANS_Caption = Clear
	TXTONE_TEXT = Clear
	TXTTWO_TEXT = Clear
End Sub

Private Sub CMDDIV_Click ()
	LBLANS_Caption = TXTONE_TEXT/TXTTWO_TEXT
End Sub

Private Sub CMDEXIT_Click ()
	End
End Sub

Private Sub CMDMINUS_Click ()
	LBLANS_Caption = TXTONE_TEXT - TXTTWO_TEXT
End Sub

Private Sub CMDMULTI_Click ()
	LBLANS_Caption = TXTONE_TEXT
End Sub