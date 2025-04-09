# HTML Color Explorer
   
## Background Story

When working with HTML, colors are an essential element that cannot be overlooked. There are multiple ways to express a single color in HTML. While many developers are comfortable with the **RGB** format, as it directly reflects the amount of each primary color (Red, Green, and Blue), it can be challenging to visualize the exact color based on arbitrary numerical values for each component.

The **HSL** format offers a more intuitive approach through the use of a color wheel. In this system, the **Hue** is represented in degrees, starting from the vertical radius at 12 o'clock (**0 degrees**), which represents red. Moving clockwise around the wheel, we find green at **120 degrees** (4 o'clock) and blue at **240 degrees** (8 o'clock). Any angle in between represents a blend of these colors. However, understanding the final color can still be complex, especially when considering **Saturation** (the intensity of the primary color components) and **Lightness** (which determines the brightness from gray to pure white).

In RGB format, there are **16,777,216** possible colors (256 x 256 x 256), commonly known as **True Color**. Despite this vast spectrum, only **144 colors** have been given standardized names in HTML.

This application aims to demonstrate the relationships between these different color formats. For instance, if you want to explore a color like *RGB(100,100,50)*, the app instantly displays its visual representation along with its corresponding HSL values (and vice versa). It also identifies the nearest named color family and allows you to experiment by clicking on different color names to see their RGB and HSL representations.

To facilitate color exploration, the application provides **sliders** for both RGB and HSL formats. These interactive controls help visualize how adjusting one component affects the others, making it easier to understand the relationship between different color representations.

## How This Application Was Created

This application emerged during my journey learning Python through **Harvard's CS50 Introduction to Programming with Python** course. While following the lectures, I was simultaneously exploring HTML, with a particular focus on CSS (*Cascading Style Sheets*). CSS proved to be a crucial component for styling web pages, with color manipulation being one of its many powerful attributes. During this period, I also discovered **FastHTML**, a modern Python framework designed for web application development.

The convergence of these three elements - **Python, CSS, and FastHTML** - inspired me to create this color exploration and simulation tool as my final project. The application represents my effort to combine these technologies while providing users with an intuitive way to experiment with colors.

This application is currently in its early development stages, and I look forward to continuing its enhancement. FastHTML proved challenging to grasp initially, as it integrates multiple technologies and frameworks. It harnesses the capabilities of **HTMX**, operates on an **ASGI** framework (Uvicorn), and comes bundled with the **PICO CSS** framework.

While developing this application, I deliberately chose not to implement the PICO CSS framework, focusing instead on deepening my understanding of HTML. This decision, however, resulted in style declarations cluttering my Python code, making it less elegant. Despite the messy appearance, this approach has significantly improved my comprehension of HTML fundamentals. In future versions, I plan to incorporate PICO (or another CSS framework) to achieve cleaner, more maintainable code.

## The Structure of this Application

This application consists of three essential files:
- **project.py** - The main application file containing core functionality and routing logic
- **warna.py** - Houses the Warna class, which represents the webpage structure in Python FastHTML format
- **kolor.py** - Contains a comprehensive dictionary of 144 color names with their corresponding RGB values

Place all three files in the same directory. No additional files are required.

I deliberately separated the web content and color dictionary into individual files to maintain a clean and organized codebase. This separation allows the main project file to remain concise, focusing primarily on routing functions that handle user interactions such as:
- Slider adjustments
- Direct RGB/HSL value inputs
- Named color selections

To run this application, follow these two simple steps:

1. Install the required module:

        pip install python-fasthtml

2. Launch the application:

        python project.py

3. Once running, access the web interface through your browser at:

        http://localhost:8000


The web page will appear as shown below:

![File ColorEx.png on the repo](https://github.com/lurah/HTML-Color-Explorer/blob/main/ColorEx.png)

## How to use this Application

Here's the enhanced version:

The web page displays three distinct sections arranged in squares - two in the upper portion and one in the lower portion, each with its own title. The first section features the **Slider**, which contains two components: the **RGB** section and the **HSL** section. Each component has three individual sliders that allow you to adjust their respective values.

The second section is the **Value Entry** part, comprising three elements. First is the **color representation**, which displays the actual color based on either RGB or HSL values (note that both slider systems are synchronized - adjusting one automatically updates the other through RGB-to-HSL or HSL-to-RGB conversion). Second is **the numerical display** of Red, Green, and Blue components corresponding to the RGB slider positions. Third is the numerical display of Hue, Saturation, and Lightness values. All components work in sync - changing any value automatically recalculates all others and updates the color representation. You can directly input values in either the RGB or HSL fields. RGB values range from 0 to 255, while HSL uses different ranges: Hue spans 0 to 360 degrees, and both Saturation and Lightness range from 0 to 100. The Value Entry system *automatically adjusts* any out-of-range inputs to the maximum allowed value for that component.

The third section focuses on **named colors**. While there are potentially **16,777,216** different colors available, only 144 have designated names. These named colors typically correspond to commonly observed colors in nature. Note that humans may not perceive subtle differences between colors with very similar component values (*such as rgb(23,24,25) versus rgb(23,24,26)*). Named colors can be categorized into approximately 10 groups with similar characteristics, with green and blue groups having the most members. This section is divided into two parts: the upper portion shows the *color group name*, while the lower portion displays *group members* with their corresponding colors. Clicking a group title reveals its members, and selecting a specific named color automatically adjusts the RGB and HSL values in the sections above.

This simulation allows you to experiment with color components while observing how changes affect both RGB and HSL values. You can explore available named colors and compare your selected colors with their nearest named counterparts.

## Additional Information

This application was developed as a final project requirement for *Harvard's CS50 Introduction to Programming with Python* course. While I strived to meet all project requirements, certain aspects, particularly the testing section, presented challenges. The main difficulty arose from using the FastHTML framework, whose functions primarily respond to browser requests and cannot be easily verified through conventional pytest methods.

I invested significant time and effort into this project, though I acknowledge some limitations in meeting the strict testing requirements. The current application's appearance remains basic, as I haven't fully utilized the CSS framework capabilities provided by FastHTML. I plan to improve both the visual presentation and code organization in the future, particularly by cleaning up the cluttered style settings.

I welcome any contributions from others interested in enhancing this application. Your involvement could help make this project more robust and visually appealing.
