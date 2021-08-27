<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_shaishulman/CompaniesHouse_Exporter">
    <img src="images/logo.png" alt="Logo">
  </a>

  <h3 align="center">CompaniesHouse exporter</h3>

  <p align="center">
    Export registration information from the UK Companies House into an Excel file  
    <!--
    <br />
    <a href="https://github.com/ShaiShulman/CompaniesHouse_Exporter"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ShaiShulman/CompaniesHouse_Exporter">View Demo</a>
    ·
    <a href="https://github.com/ShaiShulman/CompaniesHouse_Exporter/issues">Report Bug</a>
    ·
    <a href="https://github.com/ShaiShulman/CompaniesHouse_Exporter/issues">Request Feature</a>
    -->
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul> 
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!--<li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>-->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

The module receives an Excel with UK company number and adds the current registration details (name, address, directors, next confirmation statement and annual account deadlines) from the Companies House API.

The main entry point file is companies_house_exporter.py 

### Built With

* [Python 3.7](https://www.python.org/)
* [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Install all prerequisites from the included requirements.txt.

* pip install -r /path/to/requirements.txt

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_shaishulman/CompaniesHouse_Exporter.git
   ```
2. Install prerequisites
   ```sh
   pip install -r /path/to/requirements.txt
   ```
3. Apply for a developer API from the Companies House
   ```sh
   https://developer.company-information.service.gov.uk/get-started
   ```

4. Save the API into a text file named "api_key.txt" (optional)


5. Prepae an Excel file with the registration numbers of the companies you are interested in (you use xls_file_template.xlsx) 

<!-- USAGE EXAMPLES -->
## Usage

* Get directors and next deadlines information for the companies listed on "xls_file_template.xlsx" 
   ```sh
   python companies_house_exporter.py -n -d -f "xls_file_template.xlsx"
   ```

* Only get basic information and directly specify API key
   ```sh
   python companies_house_exporter.py -"xls_file_template.xlsx" -k 123456789
   ```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Shai Shulman - [@shaishulman](https://twitter.com/shaishulman) - shai.shulman@gmail.com

Project Link: [https://github.com/github_shaishulman/CompaniesHouse_Exporter](https://github.com/github_shaishulman/CompaniesHouse_Exporter)



<!-- ACKNOWLEDGEMENTS -->
<!--
## Acknowledgements

* []()
* []()
* []()
-->




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ShaiShulman/CompaniesHouse_Exporter.svg?style=for-the-badge
[contributors-url]: https://github.com/ShaiShulman/CompaniesHouse_Exporter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ShaiShulman/CompaniesHouse_Exporter.svg?style=for-the-badge
[forks-url]: https://github.com/ShaiShulman/CompaniesHouse_Exporter/network/members
[stars-shield]: https://img.shields.io/github/stars/ShaiShulman/CompaniesHouse_Exporter.svg?style=for-the-badge
[stars-url]: https://github.com/ShaiShulman/CompaniesHouse_Exporter/stargazers
[issues-shield]: https://img.shields.io/github/issues/ShaiShulman/CompaniesHouse_Exporter.svg?style=for-the-badge
[issues-url]: https://github.com/ShaiShulman/CompaniesHouse_Exporter/issues
[license-shield]: https://img.shields.io/github/license/ShaiShulman/CompaniesHouse_Exporter.svg?style=for-the-badge
[license-url]: https://github.com/ShaiShulman/CompaniesHouse_Exporter/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/shshulman/
[product-screenshot]: images/screenshot.png 