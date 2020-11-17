<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Warwick_Business_School_logo.svg/1200px-Warwick_Business_School_logo.svg.png" width="200" height="200" class="center" />
</p>

## Discovering Company-Specific Key Risk and Success Factors of Music Streaming Subscription Management by Analysing App Store Reviews: A Case Study of Tidal Music Streaming Service
***by Jung Seok Sung***

### Executive Summary

Within the intensively competitive global music streaming market, Tidal has been struggling to maintain its own streaming service. Tidal’s current financial state became highly vulnerable to the changes in the number of subscribers, as most of its revenue excessively relies on the sales of subscriptions. In order to ensure a stable subscriber base, it is necessary to recognise the current state of the service and construct proper business strategies accordingly. Therefore, this study aims to suggest a framework to diagnose key risk and success factors of Tidal’s subscription management by analysing Appstore reviews. Subscription management in this context is defined as managing the streaming service with the goal of retaining existing subscribers while attracting potential subscribers. Based on a review of the literature on key factors of premium subscription and Appstore reviews analysis, this research first collected a total of 104,743 reviews, 10,668 reviews from the Apple App Store and 94,075 reviews from the Google Play Store. Reviews text data were then properly processed for the analysis. The prepared data was then ingested into Structural Topic Modelling (STM) to figure out latent topics within the reviews. The topics are ranked through a ranking model and grouped by their origin (Apple or Google) and direction (Risk or Success). The analysis showed various company-specific key factors that threaten or strengthen the subscription management and each factor has its own characteristics in terms of topic features in the ranking model, which are topic volume, topic polarity, and topic timeliness. Based on these results, practitioners can try various interpretations of the factors and implement a more sophisticated SWOT relevant analysis to set business strategies.

### Introduction

평소 음악 산업과 음원 스트리밍 비즈니스에 관심이 많아서 이와 관련된 석사 논문을 썼습니다. 음원 스트리밍 회사 Tidal은 음원 프리미엄 구독 판매를 통한 매출이 전체 매출의 97.7%에 육박합니다. 과도하게 프리미엄 제도에 의존하는 위험한 수익 구조는 비즈니스의 존폐에 영향을 미칠 수 있다고 생각했습니다. 그래서 이 논문을 통해 안정성 있는 매출 전략 수립을 위한 Tidal 음원 스트리밍 서비스의 위험 및 성공 요소 분석 프레임워크를 제시하고자 했습니다. 음원 스트리밍은 주로 모바일 기기에서 이루어진다는 사실에 착안하여 Google Play Store와 Apple App Store에 존재하는 Tidal 앱 리뷰 텍스트 데이터를 분석함으로써 서비스의 강점과 약점을 추출했습니다.

우선 Python을 활용한 API Request를 통해 Tidal 앱에 대한 총 104,743개의 앱스토어 리뷰 데이터를 수집하고 SQLite DB 스키마에 맞게 가공한 후 저장하는 데이터 파이프라인을 구축했습니다. 그리고 R을 활용하여 TFIDF, Lemmatization, POS Tagging 등의 다양한 자연어 전처리 기법을 통해 최종적으로 51,459개의 가공된 리뷰 corpus와 215개의 명사 lexicon을 생성했습니다. 이 과정에서 Parallel Processing 관련 R 패키지들을 활용해서 데이터 전처리 속도를 380% 개선시켰습니다. 전처리가 완료된 리뷰 데이터에 Structural Topic Modeling 기법을 적용하여 총 36개의 토픽을 추출하고, 토픽들과 메타데이터 (origin, rating, date) 사이의 관계에 대해 시각화 해보면서 토픽들의 특성을 파악해 보았습니다. 마지막으로 토픽 모델링 결과치에 Ranking Model 알고리즘을 적용하여 앱스토어별 Top 5 위험/성공 토픽을 선별했습니다.

-------

Skill Set: Web Crawling/Scraping, Data Engineering, Text Pre-Processing, Structural Topic Modelling, Mathematical Algorithms<br><br>
**Full texts available - [dissertation.pdf](https://github.com/sakjung/dissertation/blob/master/dissertation.pdf)**

