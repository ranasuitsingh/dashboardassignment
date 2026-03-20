# dashboardassignment
# Used
- Playwright (Python)
- Pytest
# Scenario Covered
Login → Create Lead → Verify Lead in Dashboard

# Setup
pip install -r requirements.txt
playwright install

# Run Test
pytest tests/

# Notes
- Page Object Model used for clean structure
- Dynamic data used to avoid duplication issues
- Focused on critical business flow
