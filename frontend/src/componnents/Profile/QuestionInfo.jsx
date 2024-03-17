import CloseIcon from "@mui/icons-material/Close";
import { Box, Button, Dialog, DialogActions, DialogContent, DialogTitle, IconButton, TextField, Tooltip, Typography } from "@mui/material";
import React, { Component } from "react";
import { CharacteristicBO } from "../../api";
import CharacteristicView from "../../api/Views/CharacteristicView";
import UserProfileView from "../../api/Views/UserProfileView";


export class QuestionInfo extends Component {
    constructor(props) {
      super(props)
        let dt = true; let quName=""; let quDesc=""
        if(this.props){
            dt = this.props.question.getAuthorId() !== this.props.user.getID()
            quName = this.props.question.getName()
            quDesc = this.props.question.getDescription()
        }
      this.state = {
         disabledTextfield: dt,
         loading: false,
         success: false,
         successMessage: "",
         error: false,
         question:quName,
         description:quDesc,
         author: "Dein HeyDateMe Team"
      }
    }
    closeDialog = () => {
        this.props.closeDialog()
    }
    handleTextfieldChange = (event) => {
        this.setState({
            [event.target.id]: event.target.value
        })
    }

    deleteChar = () =>{
        CharacteristicView.getView().delete(this.props.question.getID()).then((char)=>{
            this.setState({
                success: true,
                successMessage: "Erfolgreich gelöscht"
            })
            this.props.deleteChar()
            this.props.closeDialog()

        })
        .catch((error) => console.error(error))
    }
    updateChar = () =>{
        let newCharObject = Object.assign(this.props.question, CharacteristicBO)
        newCharObject.setName(this.state.question)
        newCharObject.setDescription(this.state.description)
        CharacteristicView.getView().update(newCharObject).then((qu)=>{
            this.setState({
                loading:false,
            })
            this.props.saveChar(qu.getName())
            this.props.closeDialog()
        })
        .catch((err) => console.log("error", err));
        this.setState({
            loading: true
        })
    }
    getAuthorName = () => {
        if(this.props.question.getAuthorId() != 0){
            UserProfileView.getView().getById(this.props.question.getAuthorId()).then((author) => {
                if(author[0].firstname === "" || author[0].id === null){
                    this.setState({
                        author: "Anonym"
                    })
                }
                else{
                    this.setState({
                        author: author[0].getFirstname()
                    })
                }
            })
            .catch((err) => console.log("error", err));
        }
    }
    componentDidMount(){
        this.getAuthorName();
    }
  render() {
    const {question, open} = this.props
    return (
        <Dialog open={open}>
        <DialogTitle>
            <Typography>Details zur Eigenschaft</Typography>
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
            <DialogContent sx={{p: "3rem", display:"flex", flexDirection:"column"}}>
                <Box sx={{p:"1rem", display:"flex", gap:3, flexDirection:"column"}}>
                    <div style={{display:"flex", alignItems:"center", justifyContent:"center", gap:4}}>
                        <h4>Autor:</h4>
                        <p>{this.state.author}</p>
                        </div>
                    <Tooltip title={this.state.disabledTextfield? "Nur der Autor dieser Eigenschaft kann diese ändern": "Du kannst diese Eigenschaft ändern"}>
                <TextField
                id="question"
                disabled={this.state.disabledTextfield}
                label="Eigenschaft"
                onChange={this.handleTextfieldChange}
                value={this.state.question}
                ></TextField>
                </Tooltip>
                <Tooltip  title={this.state.disabledTextfield? "Nur der Autor dieser Eigenschaft kann diese Beschreibung ändern": "Du kannst diese Beschreibung ändern"}>
                <TextField
                id="description"
                disabled={this.state.disabledTextfield}
                label="Beschreibung"
                onChange={this.handleTextfieldChange}
                value={this.state.description}
                multiline
                rows={4}
                ></TextField>
                </Tooltip>
                </Box>
            </DialogContent>
            <DialogActions>
                {!this.state.disabledTextfield?
                <div>
                <Button onClick={this.deleteChar}>
                    Löschen
                </Button>
                <Button onClick={this.updateChar}>
                    Speichern
                </Button>
                </div>
                :null}
            </DialogActions>
        </Dialog>
        );
  }
}

export default QuestionInfo;