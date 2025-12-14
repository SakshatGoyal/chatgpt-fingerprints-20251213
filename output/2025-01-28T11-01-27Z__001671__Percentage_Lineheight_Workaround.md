# Percentage Lineheight Workaround



## You (2025-01-28T11:01:27.256461+00:00)

in figma variables, i want to set a variable for lineheight. but instead of using fixed numbers I want to use percentages -- like 100%, 120%, 135%.

I'm not able to set a numeric variable with percentage signs, and string variables are not applicable to lineheight. what are my options to continue setting percentage based variables.

## ChatGPT (2025-01-28T11:01:45.913988+00:00)

Figma currently does not natively support percentage-based variables for line height in the variables feature. The line-height property accepts only unitless numbers or fixed pixel values (e.g., 1.2, 24px), and percentage signs aren't allowed. Here's how you can work around this limitation:

### 1. **Use Unitless Numbers**
Percentage-based line heights in CSS are equivalent to unitless multipliers in Figma. For example:
- `100%` = `1.0` (multiplier)
- `120%` = `1.2`
- `135%` = `1.35`

You can create **numeric variables** in Figma for these unitless multipliers and apply them as line-height values.

#### Steps:
1. Create numeric variables for your desired line-height values.
   - `normal` = `1.0`
   - `tight` = `1.2`
   - `relaxed` = `1.35`
2. Apply these variables to text styles or directly to text objects.

---

### 2. **Create a Naming System**
If you want to use percentages for visual clarity, create a naming convention in your variable names to represent percentages:
- Variable Name: `lineheight_100`, `lineheight_120`, `lineheight_135`
- Value: `1.0`, `1.2`, `1.35`

This approach helps you maintain clarity while working within Figma's constraints.

---

### 3. **Document for Team Usage**
Add a note in your Figma file or design system documentation explaining that these unitless values represent percentages, ensuring consistency and understanding across your team.

This method keeps your design workflow efficient without losing the flexibility and intent of percentage-based line-height values.

## You (2025-01-28T11:03:05.941485+00:00)

if i use a value of 1.0, it assumes I mean 1px and not 1 percent

## ChatGPT (2025-01-28T11:03:37.860517+00:00)

You’re correct that Figma interprets `1.0` as `1px` rather than as a percentage or a relative multiplier when working with **line-height**. This is because Figma treats numeric line-height values as absolute pixel measurements unless explicitly defined as "Auto" or in some other relative context.

To work around this and ensure you can use relative percentages like `100%` or `120%`, follow these steps:

---

### **1. Use Unitless Multipliers (Alternative Interpretation of Percentage)**
While Figma does not explicitly allow percentages, **unitless values are implicitly proportional** to the font size. For example:
- **1.0 (unitless)** → 100% of the font size
- **1.2 (unitless)** → 120% of the font size
- **1.35 (unitless)** → 135% of the font size

If you enter **just the number without "px"**, Figma will calculate line-height as a proportion of the text size (not as pixels).

#### Example:
- Font Size: 16px
- Line-Height (Unitless): `1.2`
- Result: `16px × 1.2 = 19.2px` effective line-height

---

### **2. Create a Numeric Variable for Relative Values**
Set numeric variables in Figma corresponding to these unitless multipliers. For example:
- `lineheight_100` = `1.0`
- `lineheight_120` = `1.2`
- `lineheight_135` = `1.35`

Apply these numeric variables as the line-height to your text styles.

---

### **3. Avoid Fixed Pixel Values**
If you accidentally use `1` (without a decimal) or enter the value as `1px`, Figma will treat it as an absolute pixel value. To avoid this:
- Use only numbers like `1`, `1.2`, or `1.35` without `px`.
- Ensure the field recognizes it as **unitless**.

---

### **4. Testing and Adjusting**
To ensure it’s working as expected:
1. Apply your variable to a text style.
2. Change the font size of the text. The line-height will scale proportionally to the font size (e.g., 1.2 will always represent 120% of the current font size).

---

This method ensures you achieve percentage-based behavior without explicitly using percentages, as Figma inherently maps unitless numbers to font-size-relative calculations.

## You (2025-01-28T12:26:54.633637+00:00)

could u do an ocr on these color hex codes, and arrange them as a swatch for grays (gray 00. gray 10, gray 20, etc...)





## ChatGPT (2025-01-28T12:27:13.007092+00:00)

I've organized the extracted hex codes into a grayscale swatch, ranging from Gray 00 to Gray 80. You can now view the structured table. Let me know if you need any modifications!
