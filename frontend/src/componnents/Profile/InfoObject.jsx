import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import InfoIcon from '@mui/icons-material/Info';
import SaveIcon from '@mui/icons-material/Save';
import { Autocomplete, Box, CircularProgress, createFilterOptions, IconButton, TextField } from '@mui/material';
import React, { Component } from 'react';
import DescriptionBO from '../../api/DescriptionBO';
import InfoBO from '../../api/InfoBO';
import SelectionBO from '../../api/SelectionBO';
import DescriptionView from '../../api/Views/DescriptionView';
import InfoView from '../../api/Views/InfoView';
import SelectionView from '../../api/Views/SelectionView';
import AddAnswerDialog from './AddAnswerDialog';
import './Profildaten.css';
import QuestionInfo from './QuestionInfo';

const filter = createFilterOptions();
export class InfoObject extends Component {
    constructor(props) {
      super(props)
      let an = ""; 
      let ma = ""; 
      let qu = "";
      let selec = null;
      let ed = false;
      let na = false;
        if(props){
             an = this.props.answer.getAnswer()
             qu = this.props.question.getName()
             selec = this.props.answer
               if(!this.props.question.getIsSelection()){
                ma = this.props.answer.getMaxAnswer()
                na = this.props.answer.getMaxAnswer() !== ""
              }
             if (this.props.answer.getAnswer() === ""){
                ed = true;
             }
             if(!this.props.isSearchprofile){
              this.props.handleIsSaved(ed, this.props.info.getID())
            }
            }
      this.state = {
         answer: an,
         maxAnswer: ma,
         question: qu,
         editable: ed,
         saved: false,
         selectionList:[],
         selectionObject: selec,
         selectionError: false,
         openAddAnswerDialog: false,
         addAnswerSuccess: false,
         success: false,
         successMessage: "",
         loading: false,
         handleQuestionInfoBtnClicked: false,
         isNumericalAnswer: na,
         savingError: false
      }
    }

    handleEditButton = () => {
        if(this.state.editable){
          this.setState({editable: false})
          this.props.handleIsSaved(false, this.props.info.getID())
        }
        else{
          this.setState({editable: true})
          this.props.handleIsSaved(true, this.props.info.getID())
        }
    }

    closeAddDialog = () => {
      this.setState({openAddAnswerDialog: false});
    }
    handleTextFieldChange = (event) => {
        this.setState({
          [event.target.id]: event.target.value,
        });
      };
    
      saveAnimation = () => {
        this.setState({
          saved:true,
          loading: false
        })
        
        setTimeout(() => {
          this.setState({
            saved:false
          })
        }, 1200)
      }

      AddNewSelectionAnswer = () => {
        let newSelectionObject = new SelectionBO(this.props.question.getID(), this.state.answer)
        SelectionView.getView().create(newSelectionObject).then((selec) => {
          this.closeAddDialog();
          this.setState({addAnswerSuccess: true, selectionList: [...this.state.selectionList, selec], selectionObject:selec, success:true, successMessage:"Erfolgeich gespeichert"})
        })
        .catch((err) => console.log("error", err));
      }

      deleteChar = () => {
        this.props.deleteInfo(this.props.info)
      }
      deleteInfo = () => {
          InfoView.getView().delete(this.props.info.getID()).then((inf) => {
            this.setState({success: true, successMessage: "Erfolgreich gelöscht"})
            this.props.deleteInfo(this.props.info)
          })
          .catch((err) => console.log("error", err));
      }
      saveAnswer = () => {
        if(this.props.question.getIsSelection()){
          if(!this.state.selectionError){
            let newInfoObj = Object.assign( this.props.info, InfoBO)
            newInfoObj.setAnswerId(this.state.selectionObject.getID())
            InfoView.getView().update(newInfoObj).then((inf) => {
              this.saveAnimation()
            })
            .catch((err) => console.log("error", err));
            this.setState({loading:true, editable: false})
            if(!this.props.isSearchprofile){
              this.props.handleIsSaved(false, this.props.info.getID())
            }
          }
          }
          else{
            let newDescObject = Object.assign(this.props.answer, DescriptionBO )
            let maxAnswer = this.state.isNumericalAnswer ? this.state.maxAnswer === "" ?  "-" : this.state.maxAnswer : this.state.maxAnswer 
            newDescObject.setAnswer(this.state.answer);
            newDescObject.setMaxAnswer(maxAnswer)
            DescriptionView.getView().update(newDescObject).then((answ) => {
              this.setState({editable: false})
              if(!this.props.isSearchprofile){
                this.props.handleIsSaved(false, this.props.info.getID())
              }
              this.saveAnimation()
            })
            .catch((err) => console.log("error", err));
            this.setState({loading:true, editable: false})
            if(!this.props.isSearchprofile){
              this.props.handleIsSaved(false, this.props.info.getID())
            }
          }
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

      handleQuestionInfoBtnClicked = () =>{
        this.setState({
          questionInfoBtnClicked: true
        })
      }
      closeQuestionInfoBtn = () =>{
        this.setState({
          questionInfoBtnClicked: false
        })
      }
      saveChar = (newQuestion) => {
        this.setState({
          question: newQuestion
        })
      }
      componentDidMount(){
        if(this.props.question.getIsSelection()){
          SelectionView.getView().getByCharacteristic(this.props.question.getID()).then((answ) => {
            this.setState({
              selectionList:answ
            })
          })
          .catch((err) => console.log("error", err));
        }
      }

    render() {
    const {selectionList} = this.state
    return (
        <div className="eigenschaften__content-item">
        <p style={{margin:0}}>{this.state.question} 
        <IconButton onClick={this.handleQuestionInfoBtnClicked}>
          <InfoIcon/> 
          </IconButton> 
          </p>
          <QuestionInfo deleteChar={this.deleteChar} saveChar={this.saveChar}open={this.state.questionInfoBtnClicked} closeDialog={this.closeQuestionInfoBtn} user={this.props.user} question={this.props.question}/>
        <div style={{display:"flex", justifyContent:"right"}}>
        {this.props.isSelection ?
         <Box
         sx={{
           display: "flex",
           flexDirection:"column"
         }}
       >
         <Autocomplete
           renderInput={(params) => (
             <TextField {...params} label="Antwort suchen"  rowsmax={4}/>
           )}
           disabled={!this.state.editable}
           options={selectionList ? selectionList : null}
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
               (option) => inputValue.toLowerCase() === option.answer.toLowerCase()
             );
             if (inputValue !== "" && !isExisting) {
               filtered.push({
                 inputValue,
                 answer: `"${inputValue}" hinzufügen `,
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
         {this.state.selectionError ? 
         <div style={{marginLeft:"1rem", color:"red"}}>Du musst etwas auswählen!</div>
        :null}
       </Box>
      : 

      this.state.isNumericalAnswer?
          this.props.isSearchprofile?
      <div style={{display:"flex", gap:10}}>
      <TextField
      id="answer"
      onChange={this.handleTextFieldChange}
       value={this.state.answer}
       label="min"
       type="number"
       sx={{width:100}}
       disabled={!this.state.editable}
       > </TextField>
      <TextField
       id="maxAnswer"
       onChange={this.handleTextFieldChange}
       value={this.state.maxAnswer}
       label="max"
       type="number"
       sx={{width:100}}
       disabled={!this.state.editable}
       > </TextField>
       </div>
       :
        <TextField
        id="answer"
        onChange={this.handleTextFieldChange}
        value={this.state.answer}
        label="Antwort"
        sx={{ width: {xs: 200, sm: 250, md: 300, lg: 350, xl: 400}, m: 1 }}
        type="number"
        disabled={!this.state.editable}
        > </TextField>
        
        :
      <TextField
       id="answer"
       disabled={!this.state.editable}
       onChange={this.handleTextFieldChange}
       value={this.state.answer}
       multiline
       sx={{ width: {xs: 200, sm: 250, md: 300, lg: 350, xl: 400}, m: 1 }}
       > </TextField>
          }
            {this.state.editable ?
            <IconButton onClick={this.saveAnswer}>
                <SaveIcon color="secondary"/>
            </IconButton>
            :
            this.state.saved?
            <IconButton>
              <CheckCircleOutlineIcon color="success"/>
            </IconButton>
            :
            this.state.loading?
            <IconButton>
              <CircularProgress size="1.5rem"/>
            </IconButton>
            :              
            <IconButton onClick={this.handleEditButton}>
              <EditIcon color="primary"/>
            </IconButton>
            }
            {
              this.props.question.getIsStandart()?
              null
              :
            <IconButton onClick={this.deleteInfo}>
              <DeleteIcon sx={{color:"red"}}/>
            </IconButton>
            }
            </div>
            <AddAnswerDialog open={this.state.openAddAnswerDialog} closeAddDialog={this.closeAddDialog} AddNewSelectionAnswer={this.AddNewSelectionAnswer} answer={this.state.answer}></AddAnswerDialog>
    </div>
    )
  }
}

export default InfoObject