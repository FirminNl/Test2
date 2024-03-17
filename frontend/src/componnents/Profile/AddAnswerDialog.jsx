import CloseIcon from "@mui/icons-material/Close";
import { Button, ButtonGroup, CircularProgress, Dialog, DialogActions, DialogContent, DialogTitle, IconButton, Typography } from '@mui/material';
import React, { Component } from 'react';
import { SuccessMessage } from "../constants";

export class AddAnswerDialog extends Component {
constructor(props) {
  super(props)

  this.state = {
     success: false
  }
}
    closeDialog = () => {
        this.props.closeAddDialog()
    }

    handleButtonYes = () => {
        this.props.AddNewSelectionAnswer()
      this.setState({loading: true})
    }
    handleSuccessClose = () => {
        this.setState({
            success: false
        })
    }
    handleButtonNo = () => {
        this.props.closeAddDialog()
    }
  render() {
    return (
      <Dialog open={this.props.open}>
        <DialogTitle>
        <Typography>Antwort hinzufügen</Typography>
            <IconButton
              aria-label="close"
              onClick={this.closeDialog}
              sx={{
                position: "absolute",
                right: 3,
                top: 3,
              }}
            >
              <CloseIcon />
            </IconButton>
        </DialogTitle>
        <DialogContent>
            <p>Bist du dir sicher das du
              "{this.props.answer}"
              als Antwortmöglichkeit hinzufügen möchtest?</p>
        </DialogContent>
        <DialogActions>
            <ButtonGroup>

              <Button onClick={this.handleButtonYes}>
                {this.state.loading?
              <CircularProgress/>:<div>Ja</div>
            }
                </Button>
            <Button onClick={this.handleButtonNo}>Nein</Button>
            </ButtonGroup>
            <SuccessMessage  successText="Erfolgreich gespeichert!" open={this.state.success} closeSuccess={this.handleSuccessClose}/>
        </DialogActions>
      </Dialog>
    )
  }
}

export default AddAnswerDialog