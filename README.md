# Saim News App 📰

A simple Python command-line news reader that fetches live headlines from NewsAPI.

## Features

- 🗂️ 3 news categories: General, Sports, Politics
- 🌐 Fetches live news from NewsAPI
- ⏱️ Pauses 5 seconds between articles for readability
- 🛡️ Error handling for failed requests
- 🖥️ Simple CLI interface

## How to Use

### 1. Get a Free API Key

1. Go to [newsapi.org](https://newsapi.org/)
2. Click **Get API Key** (free signup)
3. Verify your email
4. Copy your API key

### 2. Add Your Key

Open `news_app.py` and replace:

```python
my_api = "YOUR_API_KEY_HERE"
```

with your real key:

```python
my_api = "abc123yourrealkey456"
```

### 3. Run the App

```bash
python news_app.py
```

### 4. Choose a Category

```
1, General news
2, Sports news
3, Political news
```

Enter 1, 2, or 3 to see headlines.

## Example Output

```
==================== Welcome to the Saim News App =====================
What is your name? Saim

========== News Categories ==========
1, General news
2, Sports news
3, Political news
Please select your category (1/2/3): 2

Welcome to Sports News, Saim

Status: 200
--- News 1 ---
Title: Team wins championship in overtime
Description: An incredible finish to the season...

--- News 2 ---
Title: Star player signs new contract
Description: The deal is worth $200 million...
```

## Requirements

Install the required library:

```bash
pip install requests
```

## What I Learned

- Working with REST APIs using `requests`
- Passing API parameters (`country`, `category`, `apikey`)
- Handling JSON responses with `.json()`
- Error handling with status codes
- String formatting with f-strings
- Time delays with `time.sleep()`

## Author

**Saim Ali** — [GitHub](https://github.com/saim-ali-analyst)

BSc in Artificial Intelligence | Aspiring Data Analyst

## License

This project is for learning purposes.