# Dream Bookshop | Python Data Analysis System

## Project Overview

Dream Bookshop is a Python-based command-line application (CLI) developed as an academic project for analysing bibliographic data and supporting data-driven decision-making.

The application processes book records and provides analytical insights into publication trends, author productivity, language distribution, publisher statistics, and missing ISBN information.

The project demonstrates practical understanding of **Python programming, Object-Oriented Programming (OOP), SOLID principles, software design patterns, data analysis, visualization, and testing methodologies**.

**Project Type:** Python CLI Data Analysis Application  
**Programming Language:** Python  
**Academic Unit:** Unit 20 – Applied Programming and Design Principles  
**Status:** Academic CLI prototype — not a production-deployed system

---

## Business Problem

Dream Bookshop requires a structured method for analysing bibliographic data to better understand its book catalogue and support future business decisions.

Manual analysis of large datasets can be time-consuming and inefficient.

The project addresses this problem through a Python-based analytical tool that processes a CSV dataset and produces numerical summaries and graphical representations.

## Application Features

The application provides six main analytical functions:

| Feature | Description |
|---|---|
| Publication Trends | Analyses the number of books published each year |
| Top Five Authors | Identifies authors with the highest publication counts |
| Language Distribution | Analyses the distribution of books across languages |
| Publisher Analysis | Identifies publishers and their publication counts |
| Missing ISBN Analysis | Identifies records with missing ISBN values and calculates percentages |
| Publications by Year and Language | Compares publishing activity by language across years |

The application uses a menu-driven command-line interface to allow users to select different analytical operations.

## Technologies and Tools

- **Python:** Application development and program logic
- **Pandas:** CSV processing, data manipulation, grouping and aggregation
- **Matplotlib:** Data visualization using charts
- **CSV:** Bibliographic dataset storage
- **UML:** Object-oriented system modelling
- **Pandas Testing Utilities:** Dataset and analytical-output validation

## Object-Oriented Programming

The application demonstrates several OOP concepts:

- Classes and objects
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism
- Method overriding and message passing

Different analytical functions are organized into separate classes, enabling modular development and a consistent way to execute analyses.

## SOLID Design Principles

The project examines the application of the five SOLID principles:

1. **Single Responsibility Principle:** Separating different data analysis functions into dedicated classes.
2. **Open/Closed Principle:** Designing analysis modules to support extension.
3. **Liskov Substitution Principle:** Using analysis objects through a shared abstraction.
4. **Interface Segregation Principle:** Keeping the analysis interface focused on a single operation.
5. **Dependency Inversion Principle:** Separating strategy execution from concrete analysis implementations.

These principles form part of the project's design methodology and evaluation.

## Software Design Patterns

### Strategy Pattern

The primary application design uses a Strategy Pattern-style approach.

The system includes an abstract `Analysis` class, concrete analytical classes, and components responsible for selecting and executing analytical operations.

This helps separate different algorithms from the menu and execution workflow.

### Additional Design Patterns

The academic report also evaluates and models other design patterns, including:

- Singleton
- Abstract Factory
- Observer
- Composite

The distinction between patterns discussed in the documentation and those present in the runnable source code is important.

## UML and System Design

The project documentation includes UML class diagrams representing the application's object-oriented architecture.

The diagrams illustrate relationships between analytical classes, abstract interfaces, strategy selection and execution components.

### Original UML Class Diagram

![Original UML Class Diagram](images/uml-class-diagram.png)

### Revised UML Design

![Revised UML Class Diagram](images/uml-modified-design.png)

## Software Testing and Validation

The project report covers a structured software testing approach, including:

- Unit testing
- Integration testing
- Regression testing
- System testing
- User acceptance testing
- Automated testing concepts using Pytest
- Data validation using Pandas

The `validation` folder contains four original Python scripts demonstrating Pandas-based data validation and analytical checks.

These scripts are separate from a complete automated Pytest suite. The presence of a testing methodology in the academic report does not imply that every proposed test has been implemented.

## Project Structure

```text
Dream-Bookshop-Python-Data-Analysis/
├── src/
│   └── Finalcode.py
├── data/
│   └── Books.csv
├── validation/
│   ├── pandas1.py
│   ├── pandas2.py
│   ├── pandas3.py
│   └── pandas4.py
├── images/
│   ├── uml-class-diagram.png
│   └── uml-modified-design.png
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Application

### Prerequisites

- Python 3
- pip

### Installation

Clone the repository:

```bash
git clone https://github.com/IsmaHaseemdeen/Dream-Bookshop-Python-Data-Analysis.git
```

Navigate into the project:

```bash
cd Dream-Bookshop-Python-Data-Analysis
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Python application:

```bash
python src/Finalcode.py
```

The application will display its login prompt, followed by the analysis menu after successful authentication.

**Note:** The source code contains demonstration login credentials. These should not be treated as production authentication or reused for real accounts.

## Skills Demonstrated

### Programming and Data Analytics

- Python Programming
- CSV Data Processing
- Data Analysis with Pandas
- Data Visualization with Matplotlib
- Analytical Problem-Solving
- Data Quality Assessment

### Software Engineering

- Object-Oriented Programming
- SOLID Principles
- Design Pattern Evaluation
- UML Class Diagrams
- Modular Programming
- Clean Coding Principles
- Software Architecture and Design

### Software Quality

- Software Testing Concepts
- Data Validation
- Test Strategy Documentation
- Debugging
- Technical Reporting

## Academic Context

This project was developed as part of **Unit 20: Applied Programming and Design Principles**, within the Pearson BTEC Higher National Diploma in Computing.

It combines a practical Python CLI prototype with academic research and documentation on object-oriented design, SOLID principles, software design patterns, and software testing.

## Disclaimer

This repository represents an academic programming project. The application is a local command-line prototype rather than a production-ready or publicly deployed business analytics platform.
