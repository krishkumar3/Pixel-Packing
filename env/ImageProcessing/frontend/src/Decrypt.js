import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { Component} from 'react';
import ReactDOM from 'react-dom';
import down_arrow from './down_arrow.png';
import axios from 'axios';
import FormData from 'form-data';




class Decrypt extends Component {
  constructor(props) {
    super(props);
    this.state = { message: '', inputImg: '', file: '', id: '' };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleImageChange = this.handleImageChange.bind(this);
  }


  handleChange(event) {
    this.setState({ [event.target.name]: event.target.value });
    console.log(this.state)

  }
  handleImageChange(event) {
    this.setState({ [event.target.name]: URL.createObjectURL(event.target.files[0]) });
    this.setState({ file: event.target.files[0] });
    console.log(this.state)

  }

  handleSubmit(event) {
    event.preventDefault();
    console.log(this.state)

      const payload = {
        "message": Number(this.state.message),
        "inputImage": this.state.inputImg,
      }

      var dataF = new FormData();
      dataF.append('inputImage', this.state.file);
      dataF.append('message', this.state.message);


      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/images/",
        data: dataF,
        headers: { "Content-Type": "multipart/form-data" },
      })

        .then(response => {
          this.setState({ status: response.status })
          this.setState({ id: [response.data.id] }, () => {
            console.log(this.state.id);
          })
          let id = response.data.id;
          let message = response.data.message;
          console.log(JSON.stringify(response.data));

          if (this.state.id != null) {
            axios({
              method: "get",
              url: "http://127.0.0.1:8000/api/images/" + id + "/",
              headers: { "Content-Type": "multipart/form-data" },
            })
              .then(response => {
                console.log(JSON.stringify(response.data));

                axios({
                  method: "post",
                  url: "http://127.0.0.1:8000/post/" + id + "/" + message +"/",
                  headers: { "Content-Type": "multipart/form-data" },
                })
                  .then(response => {
                    console.log(JSON.stringify(response.data));
                  })
                  .catch(error => {
                    console.log(error)
                  })

              })
              .catch(error => {
                console.log(error)
              })
          }


        })
        .catch(error => {
          console.log(error)
        })


  }

  render() {
    return (
      <div className="App">
        <nav class="navbar sticky-top navbar-light bg-light">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">PixSkew</a>
          </div>
          <div class="d-flex flex-row">
            <button class="btn btn-success navbar-btn me-1" onClick={event =>  window.location.href='http://127.0.0.1:8000/'}>Encrypt</button>
            <button class="btn btn-success navbar-btn" onClick={event =>  window.location.href='/decrypt'}>Decrypt</button>
          </div>
        </nav>
        <body>
          <div class="text-center">
            <h1>
              <span>Welcome</span>
              <span>To</span>
              <span>PixSkew!</span>
            </h1>
          </div>
          <div class="text-center">
            <h1 >
              <span>Send</span>
              <span>Secret</span>
              <span>Info</span>
              <span>Securely</span>
              <span>to</span>
              <span>your</span>
              <span>Friends!</span>
            </h1>
          </div>


          <div class="container center_div" style={{ maxWidth: "50vw" }}>
            <form class="formcss" onSubmit={this.handleSubmit} >


              <div class="form-group row">
                <label for="InputImage" class="col-sm-2 col-form-label" style={{ minWidth: "100px" }}>Insert Image</label>
                <div class="col-sm-4">

                  <div>
                    <img src={this.state.inputImg ? this.state.inputImg : null} alt={this.state.inputImg ? this.state.inputImg : null} class="img-thumbnail" />
                    <input type="file" name="inputImg" onChange={this.handleImageChange} required />
                  </div>
                </div>

              </div>
              <button type="submit" class="btn btn-primary" style={{ marginTop: "1vh" }}>Submit</button>
            </form>
          </div>
        </body>
      </div>
    );
  }
}
export default Decrypt;