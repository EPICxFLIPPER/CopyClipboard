import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import {Link} from "react-router-dom";


export default class CreateRoomPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: ""
        };
        this.handleRoomButtonPressed = this.handleRoomButtonPressed.bind(this);
        this.handleNameChange = this.handleNameChange.bind(this);
    }

    handleNameChange(e) {
        this.setState({
            name: e.target.value
        });
    }

    handleRoomButtonPressed() {
        console.log(this.state);
    }



    //Effects: Returns a rendering of the create room page
    render() {
        return <Grid container spacing={1}>
            <Grid item xs={12} align = "center">
                <Typography componenet='h4' variant ='h4'>
                    Create A Room!
                </Typography>
            </Grid>
            <Grid item xs={12} align = "center">
                <FormControl>
                    <TextField
                     required={true}
                     type = "string"
                     defaultValue={"Name of the Room"}
                     onChange={this.handleNameChange}
                    ></TextField>
                    <FormHelperText>
                        
                        Name of the Room
                        
                    </FormHelperText>
                </FormControl>
            </Grid>
            <Grid item xs={12} align = "center">
                <Button color = "primary" variant = "contained" onClick={this.handleRoomButtonPressed}>
                    Create Room
                </Button>
            </Grid>
            <Grid item xs={12} align = "center">
                <Button color = "secondary" variant = "contained" to="/" component={Link}>
                    Back to Home
                </Button>
            </Grid>
        </Grid>;
    }
}