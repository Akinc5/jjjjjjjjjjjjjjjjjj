from agents.gemini_agent import generate_structured_events
from utils.preprocessor import load_event_data
from agents.data_fusion import fuse_and_clean_data
from utils.news_fetcher import get_bangalore_news

if __name__ == "__main__":
    live_data = get_bangalore_news()  # 🔄 Now using NewsAPI!
    fused_data = fuse_and_clean_data(live_data)
    structured_events = generate_structured_events(fused_data)
    print("Structured Events from News Headlines:\n", structured_events)