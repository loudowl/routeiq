# RouteIQ Design Brief

## 1. Visual Identity

### Color Palette
- **Primary Color**: #1F2937 (Dark Charcoal)
- **Secondary Color**: #3B82F6 (Blue)
- **Accent Color**: #F59E0B (Amber)
- **Background Color**: #F9FAFB (Light Gray)
- **Text Color**: #111827 (Almost Black)

### Mood/Tone
The design should convey a sense of modernity, reliability, and innovation. The dark charcoal and blue provide a professional and trustworthy feel, while the amber accent adds a touch of vibrancy to highlight key elements, such as call-to-action buttons and alerts.

## 2. Typography

### Fonts
- **Heading Font**: [Roboto](https://fonts.google.com/specimen/Roboto) (Google Fonts)
- **Body Font**: [Open Sans](https://fonts.google.com/specimen/Open+Sans) (Google Fonts)

### Sizes and Weights
- **H1**: 32px, Bold
- **H2**: 28px, Bold
- **H3**: 24px, Semi-Bold
- **Body Text**: 16px, Regular
- **Buttons/Labels**: 14px, Semi-Bold

## 3. Component Library

### UI Components
- **Navigation Bar**: Horizontal layout with logo, main navigation links (Dashboard, API Docs, Pricing, Contact), and user profile dropdown.
- **Buttons**: Primary (Blue), Secondary (Charcoal), Accent (Amber) with hover and active states.
- **Cards**: For displaying savings insights and request distributions, with header, body, and footer sections.
- **Modal Dialogs**: For settings and detailed insights, with a close button and action buttons.
- **Forms**: Input fields, dropdowns, checkboxes, and radio buttons with clear labels and error messages.
- **Charts**: Line, pie, and bar charts for visualizing data insights.
- **Tables**: For displaying logs and detailed analytics, with sortable columns and pagination.
- **Notifications**: Top-right corner toast notifications for alerts and confirmations.

## 4. Key Screen Layouts

### Dashboard
- **Header**: Fixed navigation bar at the top.
- **Sidebar**: Collapsible on the left for quick access to Dashboard, API Docs, Pricing, and Profile.
- **Main Content**: 
  - **Hero Section**: Display of total savings with a large, bold number.
  - **Charts Section**: Line chart for daily cost, pie chart for model distribution, bar chart for savings.
  - **Team Controls**: Quick access to team management and settings.

### API Documentation
- **Header**: Consistent with the rest of the application.
- **Content**: Two-column layout with navigation on the left and content on the right. Code snippets and examples in a highlighted area.

### Mobile Companion App
- **Home Screen**: Display of live spend gauge and notification of budget usage.
- **Navigation**: Bottom tab bar with icons for Home, Notifications, and Settings.

## 5. Responsive Strategy

### Breakpoints
- **Mobile**: Up to 600px
- **Tablet**: 601px to 1024px
- **Desktop**: 1025px and above

Responsive design should ensure that the layout adapts to different screen sizes by using a fluid grid system and flexible images. Components should stack vertically on smaller screens and align horizontally on larger ones.

## 6. Micro-Interactions

- **Button Hover**: Slight elevation and shadow increase on hover.
- **Chart Interactions**: On hover, display tooltips with detailed information.
- **Sidebar Toggle**: Smooth slide animation when opening or collapsing.
- **Toast Notifications**: Slide in from the top-right corner and fade out after a few seconds.

## 7. Accessibility

### WCAG Considerations
- **Color Contrast**: Ensure a contrast ratio of at least 4.5:1 for text and background colors.
- **Keyboard Navigation**: All interactive elements should be accessible via keyboard.
- **Alt Text**: Provide descriptive alt text for all images and icons.
- **ARIA Labels**: Use ARIA roles and labels to enhance screen reader compatibility.
- **Focus States**: Clearly visible focus indicators for all interactive elements.

This design brief outlines the core visual and interactive elements for RouteIQ, ensuring a modern, user-friendly, and accessible experience across all platforms.