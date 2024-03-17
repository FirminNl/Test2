import CloseIcon from "@mui/icons-material/Close";
import { Autocomplete, Box, Button, ButtonGroup, CircularProgress, createFilterOptions, Dialog, DialogActions, DialogContent, DialogTitle, FormControlLabel, IconButton, Radio, RadioGroup, TextField, toggleButtonGroupClasses, Typography } from '@mui/material';
import React, { Component } from 'react';
import { DescriptionBO, InfoBO } from "../../api";
import CharacteristicBO from "../../api/CharacteristicBO";
import SelectionBO from "../../api/SelectionBO";
import CharacteristicView from "../../api/Views/CharacteristicView";
import DescriptionView from "../../api/Views/DescriptionView";
import InfoView from "../../api/Views/InfoView";
import SelectionView from "../../api/Views/SelectionView";
import { SuccessMessage } from "../constants";
import AddAnswerDialog from "./AddAnswerDialog";

const filter = createFilterOptions();

export class NewEigenschaftDialog extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         characteristicList: [],
         question: "",
         answer: "",
         maxAnswer: "-",
         charError: false,
         charObject: null,
         openAddCharDialog: false,
         success: false,
         selectionList:[],
         selectionObj: null,
         selectionError: false,
         openAddAnswerDialog: false,
         descriptionObj: null,
         successMessage: "",
         loading: false,
         answerType: "selection",
         charErrorMessage: "",
         searchProfileID: 0
      }
    }

closeDialog = () => {
    this.props.onClose()
}
closeAddDialog = () => {
    this.setState( {
        openAddCharDialog: false
    })
}
getAllCharacteristics = () =>{
    CharacteristicView.getView().getAll().then((char) => {
        this.setState( {
            characteristicList: char
        })
    })
    .catch((err) => console.log("error", err));
}

addCharacteristic = () => {
    let booleanAnswerType = this.state.answerType === "selection"
    let newCharacteristicObject = new CharacteristicBO(this.state.question, false, booleanAnswerType, this.props.user.getID(), this.state.description )
    CharacteristicView.getView().create(newCharacteristicObject).then((char) => {
        let newDescriptionObj = new DescriptionBO(char.getID(), this.state.answerType === "numeric" ? "-" : "", this.state.answer)
        DescriptionView.getView().create(newDescriptionObj).then((desc) =>{
            this.setState({
                success:true,
                characteristicList: [...this.state.characteristicList, char],
                successMessage: "Erfolgreich gespeichert!",
                loading: false,
                description:"",
                charObject: char
            })
            this.closeAddDialog()
        })
        .catch((err) => console.log("error create description",newDescriptionObj ))
        }
    )
    this.setState({loading:true})
}
handleCharacteristicChanged = (event, newValue) => {
    event.preventDefault();
   if(newValue === null){
    this.setState({charError: true, charErrorMessage:"Bitte eine Eigenschaft auswählen."})
   }
   else if(newValue instanceof CharacteristicBO){
    this.setState({charObject: newValue, charError: false, answer:""})
    if (newValue.getIsSelection()){
        this.getSelectionList(newValue)
        this.setState({
          answerType: "selection"
        })
    }
    else{
      DescriptionView.getView().getByCharacteristic(newValue.getID()).then((desc) => {
        if(desc[0].getMaxAnswer() !== "" ){
          this.setState({
            answerType: "numeric"
          })
        }
        else{
          this.setState({
            answerType: "description"
          })
        }
      })
      .catch((err) => console.log("error", err));
    }
   }
   else{
    this.setState({openAddCharDialog: true, charError: false, question: newValue.inputValue})
   }

  };

handleSuccessClose = () => {
    this.setState({
        success: false
    })
}

handleIsSelectionChange = (event) => {
this.setState({
    answerType: event.target.value
})
}
handleDescriptionChange = (event) =>{
    this.setState({
        description: event.target.value
    })
}
handleTextFieldChange = (event) =>{
    this.setState({
        [event.target.id]: event.target.value
    })
}
getSelectionList = (characteristic) => {
    SelectionView.getView().getByCharacteristic(characteristic.getID()).then((answ) => {
        this.setState({
          selectionList:answ
        })
      })
      .catch((err) => console.log("error", err));
}

closeAddSelectionDialog = () => {
    this.setState({
        openAddAnswerDialog:false
    })
}
handleSelectionChanged = (event, newValue) => {
    event.preventDefault();
   if(newValue === null){
    this.setState({selectionError: true})
   }
   else if(newValue instanceof SelectionBO){
      this.setState({selectionObject: newValue, selectionError: false})
   }
   else{
    this.setState({openAddAnswerDialog: true, selectionError: false, answer: newValue.inputValue})
   }
  };
  AddNewSelectionAnswer = () => {
    let newSelectionObject = new SelectionBO(this.state.charObject.getID(), this.state.answer)
    SelectionView.getView().create(newSelectionObject).then((selec) => {
      this.closeAddDialog();
         this.setState({success: true,successMessage: "Erfolgreich gespeichert!", selectionList: [...this.state.selectionList, selec],selectionObject:selec, openAddAnswerDialog: false,})
    })
    .catch((err) => console.log("error", err));
  }

  saveAnswer = () => {
    if(this.state.charObject){
      const isExistingCharError = this.props.questionAnswerArray.some((item) => item.question.getID() === this.state.charObject.getID())
      console.log("err",isExistingCharError, this.props.questionAnswerArray, this.state.charObject )
      if(!isExistingCharError){
      if(!this.state.charObject.getIsSelection()){
        let newDescriptionObj = new DescriptionBO(this.state.charObject.getID(), this.state.answerType === "numeric" ? this.state.maxAnswer : "", this.state.answer)
        DescriptionView.getView().create(newDescriptionObj).then((desc) =>{
          this.setState({descriptionObj: desc, success: true,successMessage: "Erfolgreich gespeichert!"})
            this.saveNewInfo(desc.getID(), false)
        })
        .catch((err) => console.log("error",newDescriptionObj ))
        this.setState({loading:true})
      }
    else{
      if(this.state.selectionObject){
        this.saveNewInfo(this.state.selectionObject.getID(), true);
        this.setState({loading:true})
      }
      else{
        this.setState({
          charError: true,
          charErrorMessage:"Du musst eine Antwort eingeben",
          loading:false
        })
      }
    }
  }
  else{
    this.setState({
      charError: true,
      charErrorMessage:"Diese Eigenschaft ist bereits in ihren Profil hinterlegt."
    })
  }
}
else{
  this.setState({
    charError: true,
    charErrorMessage:"Bitte wähl eine Eigenschaft und Antwort aus."
  })
}
  }

  saveNewInfo = (answer, isSelection) => {
    let newInfoObject = new InfoBO(this.props.profile.getID(), answer, isSelection, this.props.isSearchprofile)
    InfoView.getView().create(newInfoObject).then((info) => {
      this.setState({success: true,successMessage: "Erfolgreich gespeichert!" , loading: false, answer: "", question: "", maxAnswer:"" })
        this.props.saveInfo(info, this.state.answerType)
    })
    .catch((err) => console.log("error", err));
  }
componentDidMount(){
    this.getAllCharacteristics()
}
  render() {
    const {characteristicList} = this.state
    return (
        <>
      <Dialog open={this.props.open} onClose={this.closeDialog}>
        <DialogTitle>
        <Typography>Eigenschaft hinzufügen</Typography>
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
        <Box
         sx={{
             display: "flex",
             flexDirection:"column"
         }}
       >
         <Autocomplete
           renderInput={(params) => (
               <TextField {...params} label="Eigenschaft suchen" />
               )}
               options={characteristicList ? characteristicList : null}
               value={this.state.question}
               renderOption={(props, option) => (
                   <li {...props}>{option.name}</li>
                   )}
                   selectOnFocus
                   handleHomeEndKeys
                   sx={{ width: {xs: 200, sm: 250, md: 300, lg: 350, xl: 400}, m: 1 }}
                   freeSolo
                   clearOnEscape
                   onChange={this.handleCharacteristicChanged}
                   filterOptions={(options, params) => {
                       const filtered = filter(options, params);
   
             const { inputValue } = params;
             // Suggest the creation of a new value
             const isExisting = options.some(
                 (option) => inputValue === option.name
                 );
                 if (inputValue !== "" && !isExisting) {
                     filtered.push({
                 inputValue,
                 name: `Add "${inputValue}"`,
               });
            }
            
             return filtered;
           }}
           getOptionLabel={(option) => {
               // e.g value selected with enter, right from the input
               if (typeof option === "string") {
                   return option;
                }
                if (option.inputValue) {
                    return option.inputValue;
                }
                return option.name;
            }}
            />
       </Box>
       {this.state.charObject ?

        <Box
        sx={{
            display: "flex",
            flexDirection:"column"
        }}
        >
       {this.state.charObject.getIsSelection() ? 
         <>
       <Autocomplete
         renderInput={(params) => (
           <TextField {...params} label="Antwort hinzufügen" />
         )}
         options={this.state.selectionList ? this.state.selectionList : null}
         value={this.state.answer}
         renderOption={(props, option) => (
           <li {...props}>{option.answer}</li>
         )}
         selectOnFocus
         handleHomeEndKeys
         sx={{ width: {xs: 200, sm: 250, md: 300, lg: 350, xl: 400}, m: 1 }}
         freeSolo
         clearOnEscape
         onChange={this.handleSelectionChanged}
         filterOptions={(options, params) => {
           const filtered = filter(options, params);
 
           const { inputValue } = params;
           // Suggest the creation of a new value
           const isExisting = options.some(
             (option) => inputValue === option.answer
           );
           if (inputValue !== "" && !isExisting) {
             filtered.push({
               inputValue,
               answer: `Add "${inputValue}"`,
             });
           }
 
           return filtered;
         }}
         getOptionLabel={(option) => {
           // e.g value selected with enter, right from the input
           if (typeof option === "string") {
             return option;
           }
           if (option.inputValue) {
             return option.inputValue;
           }
           return option.answer;
         }}
       />
       <AddAnswerDialog open={this.state.openAddAnswerDialog} answer={this.state.answer}closeAddDialog={this.closeAddSelectionDialog} AddNewSelectionAnswer={this.AddNewSelectionAnswer}/>
       {this.state.selectionError ? 
       <div style={{marginLeft:"1rem", color:"red"}}>Du musst etwas auswählen!</div>
      :null}
      </>
      :
      this.state.answerType === "numeric" ?
        this.props.isSearchprofile ?
      <div>
      <TextField
      id="answer"
      onChange={this.handleTextFieldChange}
      value={this.state.answer}
      sx={{width:200, m: 1}}
      label="Min"
      type="number"
     > </TextField>
      <TextField
      id="maxAnswer"
      onChange={this.handleTextFieldChange}
      value={this.state.maxAnswer}
      sx={{width:200, m: 1}}
      label="Max"
      type="number"
      > </TextField>
      </div>
     :
     <TextField
     id="answer"
     onChange={this.handleTextFieldChange}
     value={this.state.answer}
     sx={{width:200, m: 1}}
     label="Antwort"
     type="number"
    > </TextField>
     :
      <TextField
      id="answer"
      onChange={this.handleTextFieldChange}
      value={this.state.answer}
      sx={{width:{xs: 200, sm: 250, md: 300, lg: 350, xl: 400}, m: 1}}
      label="Antwort"
     > </TextField>
       }
       </Box>
    :null}
    {this.state.charError?
    <p style={{color:"red"}}>{this.state.charErrorMessage}</p>
  :null}
        </DialogContent>
        <DialogActions>
            <Button onClick={this.saveAnswer}>
              {
                this.state.loading?
                <CircularProgress/>
                : <div>
                  Speichern
                </div>
              }
            </Button>
        </DialogActions>
      </Dialog>
      <Dialog open={this.state.openAddCharDialog} onClose={this.closeAddDialog}>
        <DialogTitle>
        <Typography>Neue Eigenschaft erstellen</Typography>
            <IconButton
              aria-label="close"
              onClick={this.closeAddDialog}
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
       <p>Welche Art der Antwort bevorzugst du zu deiner neuerstellten Eigenschaft:
        </p>
        <p style={{fontWeight:"bold"}}>
        "{this.state.question}"
        </p>
        <RadioGroup
        aria-labelledby="demo-controlled-radio-buttons-group"
        name="controlled-radio-buttons-group"
        value={this.state.answerType}
        onChange={this.handleIsSelectionChange}
      >
        <FormControlLabel value={"selection"} control={<Radio />} label="Auswahlmöglichkeiten" />
        <FormControlLabel value={"description"} control={<Radio />} label="Freitext" />
        <FormControlLabel value={"numeric"} control={<Radio />} label="Zahl" />
      </RadioGroup>
      <p>Füge deiner Eigenschaft noch eine kurze Beschreibung hinzu:</p>
      <TextField
      id="outlined-multiline-static"
      label="Beschrebung"
      multiline
      rows={4}
      value={this.state.description}
      onChange={this.handleDescriptionChange}
      sx={{width:"100%"}}>

      </TextField>
        </DialogContent>
        <DialogActions>
            <ButtonGroup>
              {this.state.loading?
              <CircularProgress size="2.3rem"/>
              :<Button onClick={this.addCharacteristic}>Speichern</Button>
            }
            <Button onClick={this.closeAddDialog}>Abbrechen</Button>
            </ButtonGroup>
            <SuccessMessage  successText={this.state.successMessage} open={this.state.success} closeSuccess={this.handleSuccessClose}/>
        </DialogActions>
      </Dialog>
    </>
    )
  }
}

export default NewEigenschaftDialog