# Markdown to PDF Converter Test Suite

## 1. Basic Markdown Features

### 1.1 Headings
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

### 1.2 Text Formatting
This is **bold text** and this is *italic text*.
Here's some `inline code` and ***bold italic*** text.

### 1.3 Lists
1. First ordered item
2. Second ordered item
   - Nested unordered item
   - Another nested item
3. Third ordered item

- Unordered list
- With multiple items
  1. Nested ordered item
  2. Another nested item

### 1.4 Code Blocks
```python
def hello_world():
    print("Hello, World!")
    return True

# This is a comment
class TestClass:
    def __init__(self):
        self.value = 42
```

### 1.5 Blockquotes
> This is a blockquote
> With multiple lines
>> And nested quotes

## 2. Table Tests

### 2.1 Simple Table
| Name | Age | City |
|------|-----|------|
| John | 30  | New York |
| Jane | 25  | London |

### 2.2 Wide Table
| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
|----------|----------|----------|----------|----------|----------|----------|----------|
| Data 1   | Data 2   | Data 3   | Data 4   | Data 5   | Data 6   | Data 7   | Data 8   |
| More 1   | More 2   | More 3   | More 4   | More 5   | More 6   | More 7   | More 8   |

### 2.3 Table with Long Content
| Feature | Description |
|---------|-------------|
| Feature 1 | This is a very long description that should wrap properly within the cell without breaking the layout or making the table too wide for the page. |
| Feature 2 | Another lengthy description that demonstrates how the table handles long content and maintains readability while ensuring proper formatting. |

### 2.4 Numeric Table
| ID | Value | Percentage |
|----|--------|------------|
| 1  | 100.00 | 50.5% |
| 2  | 200.50 | 75.8% |
| 3  | 300.75 | 90.2% |

## 3. Page Break Test

### 3.1 Multiple Pages
This section tests page breaks with multiple pages of content.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

[Repeat the above paragraph 5 times to test page breaks]

### 3.2 Table Across Pages
| ID | Description |
|----|-------------|
| 1  | Item 1 Description |
| 2  | Item 2 Description |
| 3  | Item 3 Description |
| 4  | Item 4 Description |
| 5  | Item 5 Description |
| 6  | Item 6 Description |
| 7  | Item 7 Description |
| 8  | Item 8 Description |
| 9  | Item 9 Description |
| 10 | Item 10 Description |
| 11 | Item 11 Description |
| 12 | Item 12 Description |
| 13 | Item 13 Description |
| 14 | Item 14 Description |
| 15 | Item 15 Description |

## 4. Links and Images
[OpenAI Website](https://www.openai.com)
![Sample Image](https://via.placeholder.com/150)

## 5. Horizontal Rules
Above the line

---

Below the line

***

Another line

___

## Test Completion Checklist
- [ ] Basic Markdown features render correctly
- [ ] Tables display properly with various content types
- [ ] Page breaks work as expected
- [ ] Links are clickable in the PDF
- [ ] Images are displayed correctly
- [ ] Font sizes are consistent
- [ ] Margins are correct (2.5cm)
- [ ] Page numbers are present
- [ ] Headers repeat on new pages for tables
- [ ] Code blocks maintain formatting
