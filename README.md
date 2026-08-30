# 🐍 PythonBrainstorm

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Package Manager](https://img.shields.io/badge/package%20manager-uv-blueviolet.svg)](https://github.com/astral-sh/uv)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**PythonBrainstorm** is a structured repository of Python scripts, data science notebooks, competitive programming solutions, coursework, and mini-projects. It reflects continuous learning, best practices, and explorations across the Python ecosystem.

---

## 📂 Repository Structure

```tree
PythonBrainstorm/
├── algorithms/                    # Data structures & search/sort algorithms
│   ├── ReadMe.md
│   ├── app.py
│   ├── binary_search.py
│   ├── bubble_sort.py
│   ├── linear_search.py
│   ├── selection_sort.py
│   └── unit_testing__pytest.py
├── competitive_programming/       # Problem-solving platforms
│   ├── hackerrank/                # HackerRank problem solutions
│   │   ├── nested_list.py
│   │   └── runner_up.py
│   ├── interviewbit/              # InterviewBit problem solutions
│   │   └── majority-element.py
│   └── leetcode/                  # LeetCode problem solutions
│       ├── add_binary.py
│       ├── index_of_string.py
│       ├── is_subsequence.py
│       ├── length_of_last_word.py
│       ├── longest_common_prefix.py
│       ├── merge_intervals.py
│       ├── merge_sorted_array.py
│       ├── merge_two_list.py
│       ├── plus_one.py
│       ├── remove_duplicates.py
│       ├── remove_element.py
│       ├── roman_to_integer.py
│       ├── search_insert_position.py
│       ├── sqrt.py
│       └── two_sum.py
├── core_concepts/                 # Core Python language concepts
│   └── type_annotations/         # Static typing and type hints
│       ├── basic_typing.py
│       └── practice.py
├── courses_and_books/             # Coursework, academic labs & book exercises
│   ├── ai_lab/                    # Artificial Intelligence Lab notebooks & datasets
│   │   ├── AI_L1_Intro_colab_12_8_23.ipynb
│   │   ├── AI_L2_loop_26_8_23.ipynb
│   │   ├── AI_L4_pandas_2_9_23.ipynb
│   │   ├── AI_L5_practice_16_9_23.ipynb
│   │   ├── batch_dept.xlsx
│   │   └── demo.csv
│   ├── meta_backend/              # Meta Back-End Course code & modules
│   │   ├── logarithmic_time.py
│   │   └── w4_modules/
│   │       ├── filechanges.py
│   │       ├── reloads.py
│   │       └── sample.py
│   └── tss_python/                # Tamim Shahriar Subeen Python series exercises
│       ├── advanced/              # Generators, primes, async, decorators, etc.
│       │   ├── async_basic.py
│       │   ├── c1_generator.py
│       │   ├── c1_prime_generator.py
│       │   ├── c1_prime_normal_method.py
│       │   ├── common_arr.py
│       │   ├── count_number.py
│       │   ├── decorators_basic.py
│       │   └── json_basic.py
│       └── oop/                   # Object-Oriented Programming exercises
│           ├── ch2_fibo.py
│           ├── ch3_class.py
│           ├── ch6_Inheritance.py
│           ├── ch6_method_overriding.py
│           ├── ch6_supper.py
│           ├── country/
│           ├── cpbook.pdf
│           └── cpbook.py
├── data_science_notebooks/        # Jupyter Notebooks & Data Science explorations
│   ├── housing.ipynb
│   ├── image-classifier.ipynb
│   ├── matplotlib.ipynb
│   ├── population.ipynb
│   ├── python_maateen.ipynb
│   ├── Python_Notes.ipynb
│   ├── USA_Housing.csv
│   └── atlantis.csv
└── projects/                      # Mini applications and experimental tools
    ├── chatgpt_explorations/      # OpenAI / NLP / SpaCy experiments
    │   ├── nlp_basic.py
    │   ├── nlp_practice.py
    │   ├── playground.py
    │   └── spacy_basic.py
    └── mini_projects/             # Standalone Python scripts & games
        ├── dice_simulator.py
        └── number_guessing_game.py
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/)

### Installation & Environment Setup with `uv`

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GaziAshiq/PythonBrainstorm.git
   cd PythonBrainstorm
   ```

2. **Sync the virtual environment and dependencies:**
   ```bash
   uv sync
   ```

3. **Add new dependencies:**
   ```bash
   uv add <package_name>
   ```

---

## 🧪 Testing & Quality Assurance

Run tasks using `uv run`:

- **Run Pytest:**
  ```bash
  uv run pytest
  ```
- **Type Checking (MyPy):**
  ```bash
  uv run mypy core_concepts/
  ```

---

## 🤝 Contributing

Contributions, issues, and feature suggestions are welcome! Feel free to check out the issues page or open a pull request.
