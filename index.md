## Are women better than men at multi-tasking?

Recreating the experiment presented in Stoet et al. (2013).

### Project

The project consisted in replicating the paper (Stoet et al.) which tried to verify the common belief that women are better at multi-tasking than men. To check this, they designed two experiments. In the first one, computer-based task switching paradigm was used, and in the second one, paper-and-pencil multi-tasking tests were used.

According to Stoet et al. (2013), multi-tasking can be defined in two ways: as performing several tasks sequentially/interchangeably or as performing several tasks simultaneously. It is the first sense that is used in the part of the paper by Stoet et al. (2013) that we reproduced. Here, multi-tasking ammounted to task-switching.

We only reproduced Experiment 1, because Experiment 2 wasn’t computer-based at all; it aimed to create a "real-life" multi-tasking situation and used standardized neuro-cognitive tests.

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### The experiment

The main concept of the experiment is responding to the location and the form of stimuli: 1. differentiating between diamonds and squares (if the stimuli appears bellow "Shape") by pressing the LEFT arrow key for a diamond and the RIGHT arrow key for a square and 2. differentiating between the number (2 or 3) of dots inside the figure (if the stimuli appears above "Filling") by pressing the LEFT arrow key for two dots and the RIGHT arrow key for three dots. First, the experiment is divided in two parts: training and the real experiment (where the actual data are collected). Each part consists of three blocks of trials (40 each for training and 64 each in the real experiment). In the first block, subjects only differentiate between diamonds and squares and in the second block they only differentiate between the number of dots in the figures (2 or 3). It is only in the third block that the real experiment starts: figures randomly (and intechangeably) appear either bellow "Shape" or above "Filling" which determines whether the subject has to focus on shapes or dots and press the key accordingly.

### Our implementation

Even thought the order was identical for all participants, we decided to provide the possibility of randomising it, also because it is much easier to just use it once to generate it if you want.

Quite obviously, the code isn't as clear as it could be

### Running the experiment 

The stimuli have to be downloaded too
