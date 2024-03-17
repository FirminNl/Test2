import CloseIcon from "@mui/icons-material/Close";
import SendIcon from '@mui/icons-material/Send';
import { Dialog, DialogContent, DialogTitle, IconButton, TextField, Typography } from '@mui/material';
import React, { Component } from 'react';
import MessageBO from "../api/MessageBO";
import MessageView from "../api/Views/MessageView";
import "./ChatDialog.css";

export class ChatDialog extends Component {
  chatInterval = 0;
    constructor(props) {
      super(props)

      this.state = {
         message: "",
         messageList: [],
        loading: false

      }
    }

    componentDidMount() {
      this.getAllMessagesInterval();
    }

    componentWillUnmount() {
      if (this.chatInterval) {
        clearInterval(this.chatInterval);
      }
    }

    getAllMessagesInterval = () => {
      if (this.chatInterval) {
        clearInterval(this.chatInterval);
      }
      this.chatInterval = setInterval(this.getMessages, 3500);
    };

    getMessages = () => {
      MessageView.getView()
        .getByChatId(this.props.chat.getID())
        .then((mes) => {
          this.setState({
            messageList: mes,
            loading: false,
          });
        })
        .catch((error) => {
          // Handle error if any
          console.log(error);
        });
      this.setState({
        loading: true,
      });
    };

    createMessage = () => {
      let newMessageObj = new MessageBO(
        this.props.chat.getID(),
        this.state.message,
        this.props.user.getID()
      );
      MessageView.getView()
        .create(newMessageObj)
        .then((mes) => {
          this.setState({
            message: "",
            messageList: [...this.state.messageList, mes]
          });
        })
        .catch((error) => {
          // Handle error if any
          console.log(error);
        });
    };

    closeDialog = () => {
      clearInterval(this.chatInterval);
      this.props.handleClose();
    };

    handleMessageChange = (event) => {
      this.setState({
        [event.target.id]: event.target.value,
      });
    };

    handleKeyDown = (event) => {
      if (event.key === 'Enter') {
        this.createMessage();
      }
    };

    transformDatetime = (dateString) => {
      const newDate = new Date(dateString)
      const formattedTime = newDate.toLocaleTimeString('de-DE', { hour12: false, month:'2-digit', day:'2-digit' , hour: '2-digit', minute: '2-digit' });
      return formattedTime
    }

  render() {
    return (
      <Dialog open={this.props.open}>
        <DialogTitle>
        {this.props.candidate ?
        <Typography>
        {this.props.candidate.getFirstname()}
        {this.props.candidate.getSurname()} </Typography>
        :null}
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
        <DialogContent sx={{p:0}}>
          <div className="chat-field">
            <div className="chat-field-wrapper" >
            {this.state.messageList.map((item)=>
              <div style={{display: "flex", flexDirection:"column", alignItems: this.props.user.getID() === item.getSenderId()? "flex-end" : "flex-start"}}>
            <div className="message-item" style={{backgroundColor:this.props.user.getID() === item.getSenderId()? "#6CB5FF" : "#929292"}}>
            <div className="message-item-content">
              <div className="message-item-content-text">
              {item.getContent()} 
              </div>
              <div className="message-item-content-time">
                {this.transformDatetime(item.getTimestamp())}
                </div>
              </div>
            </div>
              </div>
            )}
            </div>
          <div className="message-field">
              <TextField sx={{zIndex:99, backgroundColor:"white", width:"350px"}}
              value={this.state.message}
              id="message"
              onChange={this.handleMessageChange}
              onKeyDown={this.handleKeyDown}/>
              <IconButton onClick={this.createMessage}>
              <SendIcon color="#6CB5FF" sx={{fontSize: {xs: 20, sm: 35, md: 40, lg: 45, xl: 50}}}/>
              </IconButton>
          </div>
          </div>
        </DialogContent>
      </Dialog>
    )
  }
}

export default ChatDialog