import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import BlockIcon from '@mui/icons-material/Block';
import BookmarkAddIcon from '@mui/icons-material/BookmarkAdd';
import BookmarkRemoveIcon from '@mui/icons-material/BookmarkRemove';
import CloseIcon from "@mui/icons-material/Close";
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import HighlightOffIcon from '@mui/icons-material/HighlightOff';
import PersonAddIcon from '@mui/icons-material/PersonAdd';
import UndoIcon from '@mui/icons-material/Undo';
import { Button, CircularProgress, Dialog, DialogContent, DialogTitle, IconButton, Typography } from '@mui/material';
import React, { Component } from 'react';
import { BlockedProfileBO, ChatBO } from '../../api';
import MemoBoardBO from '../../api/MemoBoardBO';
import BlockedProfileView from '../../api/Views/BlockedProfileView';
import ChatView from '../../api/Views/ChatView';
import MemoBoardView from '../../api/Views/MemoBoardView';
import { SuccessMessage } from '../constants';


export class ProfileDetailsPopUp extends Component {
    constructor(props) {
      super(props)

      this.state = {
        success: false,
        successMessage: ""
      }
    }
    addUser = () =>{
      let newChatObject = new ChatBO(this.props.user.getID(), this.props.candidateID, false, true)
      ChatView.getView().create(newChatObject).then((chat) => {
        this.setState({
          success: true,
          successMessage:"Anfrage erfolgreich verschickt!"
        });
        this.props.removeEntry(this.props.parentObject, "Anfrage erfolgreich verschickt!");
      })
      .catch((err) => console.log("error", err));
      this.setState({
        loading: true,
      })
    }
    closeDialog = () =>{
      this.props.handleClose();
    }

    markUser = () => {
      let newMemoObject = new MemoBoardBO(this.props.user.getID(), this.props.candidateID)
      console.log("new", newMemoObject)
      MemoBoardView.getView().create(newMemoObject).then(() =>{
          this.setState({
            success: true,
            successMessage:"User Erfolgreich gemerkt!"
          })
          this.props.removeEntry(this.props.parentObject, "User Erfolgreich gemerkt!")
      })
      .catch((err) => console.log("error", err));
    }

    handleCloseSuccess = () => {
      this.setState({
        success: false
      })
    }

    blockUser = () => {
      let newBlockUser = new BlockedProfileBO(this.props.user.getID(), this.props.candidate.getID())
      BlockedProfileView.getView().create(newBlockUser).then(() =>{
          this.setState({
            success: true,
            successMessage:"User erfolgreich geblockt!"
          })
          this.props.removeEntry(this.props.parentObject, "User erfolgreich geblockt!")
      })
      .catch((err) => console.log("error", err));
    }

    deleteRequest = () => {
      ChatView.getView().delete(this.props.parentObject.getID()).then(() =>{
          this.setState({
            success: true,
            successMessage:"Anfrage erfolgreich zurückgezogen!"
          })
          this.props.removeEntry(this.props.parentObject, "Anfrage erfolgreich zurückgezogen!")
      })
      .catch((err) => console.log("error", err));
    }

    acceptRequest = () => {
      let newChatObject = Object.assign(this.props.parentObject, ChatBO)
      newChatObject.setAccepted(true)
      newChatObject.setIsOpen(false)
      ChatView.getView().update(newChatObject).then((chat)=>{
        this.setState({
            success: true,
            successMessage:"Anfrage erfolgreich angenommen!"
        })
        this.props.removeEntry(this.props.parentObject, "Anfrage erfolgreich angenommen!")
      })
      .catch((err) => console.log("error", err));
    }

    deleteMark = () => {
      MemoBoardView.getView().delete(this.props.parentObject.getID()).then((obj)=>{
        this.setState({
            success: true,
            successMessage:"Merkung erfolgreich gelöscht!"
        })
        this.props.removeEntry(this.props.parentObject, "Merkung erfolgreich gelöscht!")
      })
      .catch((err) => console.log("error", err));
    }

    deleteBlock = () => {
      BlockedProfileView.getView().delete(this.props.parentObject.getID()).then((obj)=>{
        this.setState({
            success: true,
            successMessage:"Blockierung erfolgreich gelöscht!"
        })
        this.props.removeEntry(this.props.parentObject, "Blockierung erfolgreich gelöscht!")
      })
      .catch((err) => console.log("error", err));
    }
  render() {
    return (
      <>
        <SuccessMessage open={this.state.success} closeSuccess={this.handleCloseSuccess} successText={this.state.successMessage}/>
      <Dialog open={this.props.open} >
        <DialogTitle>
        <Typography>
        {this.props.candidate ?
        <div>
        <h2 style={{marginBottom:0}}>{this.props.candidate.getFirstname()} {this.props.candidate.getSurname()}</h2>
        <p style={{margin:0, display:"flex", alignItems:"center"}}> <ArrowForwardIosIcon/>{this.props.candidate.getAboutMe()}</p>
        </div>
        :null}
        </Typography>
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
        <DialogContent sx={{width:"500px"}}>
              <div className="popup-wrapper">
                <div>
        {this.props.questionAnswerArray.map((item)=>
          <div className="card-attr" key={item.question.getID()}>
          <h2 className="card-attr-name">{item.question.getName()}</h2>
            <p className="card-attr-value">{item.answer.getAnswer()}</p>
          </div>
        )}
        </div>
        {this.props.parentComponent === "match" ?
        <div className="popup-button-group">
        <Button variant="contained" onClick={this.addUser} startIcon={this.state.addLoading? <CircularProgress/> : <PersonAddIcon/>}>
          {this.state.addLoading ? "LOADING..." : "Chat Anfrage"}
        </Button>
        <Button sx={{backgroundColor:"#E1A100", ":hover": {bgcolor: "#E1A100",}}} variant="contained" onClick={this.markUser} startIcon={this.state.markLoading? <CircularProgress/> : <BookmarkAddIcon/>}>
          {this.state.markLoading ? "LOADING..." : "Merken"}
        </Button>
        <Button color="error" variant="contained" onClick={this.blockUser} startIcon={this.state.blockLoading? <CircularProgress/> : <BlockIcon/>}>
        {this.state.blockLoading ? "LOADING..." : "Blocken"}
        </Button>
          </div>
          :
          this.props.parentComponent === "gesendeteAnfrage" ?
        <div className="popup-button-group">

        <Button color="secondary" variant="contained" onClick={this.deleteRequest} startIcon={this.state.markLoading? <CircularProgress/> : <UndoIcon/>}>
        {this.state.markLoading ? "LOADING..." : "Anfrage zurückziehen"}
        </Button>
        <Button color="error" variant="contained" onClick={this.blockUser} startIcon={this.state.blockLoading? <CircularProgress/> : <BlockIcon/>}>
        {this.state.blockLoading ? "LOADING..." : "Blocken"}
        </Button>
          </div>
          :
          this.props.parentComponent === "empfangeneAnfrage" ?
          <div className="popup-button-group">
        <Button variant="contained" onClick={this.acceptRequest} startIcon={this.state.addLoading? <CircularProgress/> : <PersonAddIcon/>}>
          {this.state.addLoading ? "LOADING..." : "Anfrage annehmen"}
        </Button>
        <Button sx={{backgroundColor:"#880000", ":hover": {bgcolor: "#880000",}}} variant="contained" onClick={this.deleteRequest} startIcon={this.state.markLoading? <CircularProgress/> : <HighlightOffIcon/>}>
        {this.state.markLoading ? "LOADING..." : "Anfrage ablehnen"}
        </Button>
        <Button color="error" variant="contained" onClick={this.blockUser} startIcon={this.state.blockLoading? <CircularProgress/> : <BlockIcon/>}>
        {this.state.blockLoading ? "LOADING..." : "Blocken"}
        </Button>
          </div>
          :
          this.props.parentComponent === "activeChats" ?
          <div className="popup-button-group">
          <Button sx={{backgroundColor:"#880000", ":hover": {bgcolor: "#880000",}}} variant="contained" onClick={this.deleteRequest} startIcon={this.state.markLoading? <CircularProgress/> : <DeleteForeverIcon/>}>
            {this.state.markLoading ? "LOADING..." : "Chat löschen"}
          </Button>
          <Button color="error" variant="contained" onClick={this.blockUser} startIcon={this.state.blockLoading? <CircularProgress/> : <BlockIcon/>}>
          {this.state.blockLoading ? "LOADING..." : "Blocken"}
          </Button>
            </div>
            :
            this.props.parentComponent === "blocked" ?
            <div className="popup-button-group">
            <Button variant="contained" onClick={this.deleteBlock} startIcon={this.state.addLoading? <CircularProgress/> : <PersonAddIcon/>}>
              {this.state.addLoading ? "LOADING..." : "Entblocken"}
            </Button>
              </div>
              :
              this.props.parentComponent === "marked" ?
              <div className="popup-button-group">
              <Button variant="contained" onClick={this.addUser} startIcon={this.state.addLoading? <CircularProgress/> : <PersonAddIcon/>}>
                {this.state.addLoading ? "LOADING..." : "Anfrage schicken"}
              </Button>
              <Button sx={{backgroundColor:"#E1A100", ":hover": {bgcolor: "#E1A100",}}}  variant="contained" onClick={this.deleteMark} startIcon={this.state.markLoading? <CircularProgress/> : <BookmarkRemoveIcon/>}>
              {this.state.markLoading ? "LOADING..." : "Markierung aufheben"}
              </Button>
              <Button color="error" variant="contained" onClick={this.blockUser} startIcon={this.state.blockLoading? <CircularProgress/> : <BlockIcon/>}>
              {this.state.blockLoading ? "LOADING..." : "Blocken"}
              </Button>
                </div>
                :null
          }
        </div>
        </DialogContent>
      </Dialog>
              </>
    )
  }
}

export default ProfileDetailsPopUp