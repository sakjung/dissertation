# load("ranking_model_origin_result.rda")

read.csv("less_than_30.csv", encoding = "UTF-8") %>% summarise(mean(rating))
 
topic_timewindow_origin %>% filter(origin==1) %>% select(timewindow) %>% unique() %>% pull()
topic_timewindow_origin %>% filter(origin==2) %>% select(timewindow) %>% unique() %>% pull()


# negative ranking
data_for_rank_norm_apple %>% 
  filter(direction < 0) %>%
  arrange(desc(score_norm)) %>% 
  head(5) %>% 
  View() 
data_for_rank_norm_google %>% 
  filter(direction < 0) %>%
  arrange(desc(score_norm)) %>%
  head(5) %>% 
  View()

# positive ranking
data_for_rank_norm_apple %>% 
  filter(direction > 0) %>%
  arrange(desc(score_norm)) %>%
  head(5) %>%
  View()
data_for_rank_norm_google %>% 
  filter(direction > 0) %>%
  arrange(desc(score_norm)) %>%
  head(5) %>%
  View()
