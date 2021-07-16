<br />
<p align="center">
  <a href="https://github.com/roshanlam/HonorsPy/">
    <img src="./SearchItLogo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Search Engine</h3>
  <p align="center">
    A Search Engine (This is the development branch, please check the main branch for the stable version) for one of my honors project, this is the first honors project.
    <br />
    <br />
    <br />
    <a href="">View The Search Engine</a>
    ·
    <a href="https://github.com/roshanlam/HonorsPy/issues">Report Bug</a>
    ·
    <a href="https://github.com/roshanlam/HonorsPy/issues">Request Feature</a>
    ·
    <a href="https://github.com/roshanlam/HonorsPy/pulls">Send a Pull Request</a>
  </p>
  <div align="center">
    <img src="https://travis-ci.org/roshanlam/HonorsPy.svg?branch=dev"/>
  </div>
  
<!-- ABOUT THE PROJECT -->
<h2> About The Project </h2>
It's a search engine that gives you control for your privacy, no ads, no bias results. Just results.


### Built With
- [x] Python
- [x] Django
- [x] HTML
- [x] CSS
- [x] Bootstrap
- [x] JS
- [ ] NextJS (In Progress)
<h3> Prerequisites </h3>

* Python
* Django
* Node
* ReactJS
* NextJS  
* Docker
* Docker Compose

### Installation

#### Frontend

1. `git clone https://github.com/roshanlam/HonorsPy`
2. `cd frontend`
If doing dev work run #3 and skip 4 & 5. Do not run #3 if not doing dev work.
3. `npm run dev`
4. `npm run build`
5. `npm start`


#### Backend
1. `git clone https://github.com/roshanlam/HonorsPy`
2. `cd HonorsPy`
3. `docker-compose build`
4. `docker-compose up`
5. Go to `http://0.0.0.0:8000/`, that's where search engine will be.

<!-- ROADMAP -->
## 🚧 Roadmap

See the [open issues](https://github.com/roshanlam/HonorsPy/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## 🤝 Contributing
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes, Please Keep MVC in mind (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## 📝 License
- [ ] Need To Choose A License

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* Aakash Japi - used his code from his blog called "Implementing a Search Engine with Rankings in Python" for search.py 
  
http://aakashjapi.com/fuckin-search-engines-how-do-they-work/


## ToDo
- [x] Work on the actual search functionality 
- [x] Store User's basic Information in a json file 
- [x] Show User's basic Information on url/seeHistory/Crawl and url/seeHistory/Query
- [x] Successfully Finish Working on Github Actions
- [x] Logo Design
- [ ] Let User's Login and SignUp and View Their Search/Crawl History from anywhere.
- [ ] Improve the main search and crawler code for better information retrieval from websites and better ranking as well as returning multiple returns instead of one
- [ ] Add NextJS For The FrontEnd
