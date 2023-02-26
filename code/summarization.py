import nltk
from functions.get_summary import summarize
from functions.parse_pdf import parse_pdf
from functions.parse_audio import parse_audio, video_to_audio
from functions.preprocessing import preprocessing
from functions.call_chat_gpt import paraphrase
# import moviepy.editor

doc1 = "Text summarization &&& is the process of automatically creating a compressed version of a given text that provides useful information for the user. In this pa- per, we focus on multi-document generic text sum- marization, where the goal is to produce a summary of multiple documents about the same, but unspecified topic. Our summarization approach is to assess the cen- trality of each sentence in a cluster and include the most important ones in the summary. In Section 2, we present centroid-based summarization, a well- known method for judging sentence centrality. Then we introduce two new measures for centrality, De- gree and LexPageRank, inspired from the “prestige” concept in social networks and based on our new ap- proach. We compare our new methods and centroid- based summarization using a feature-based generic summarization toolkit, MEAD, and show that new features outperform Centroid in most of the cases. Test data for our experiments is taken from Docu- ment Understanding Conferences (DUC) 2004 sum-marization evaluation to compare our system also with other state-of-the-art summarization systems.Extractive summarization produces summaries by choosing a subset of the sentences in the original documents. This process can be viewed as choosing the most central sentences in a (multi-document) cluster that give the necessary and enough amount of information related to the main theme of the clus- ter. Centrality of a sentence is often defined in terms of the centrality of the words that it contains. A common way of assessing word centrality is to look at the centroid. The centroid of a cluster is a pseudo- document which consists of words that have fre- quency*IDF scores above a predefined threshold. In centroid-based summarization (Radev et al., 2000), the sentences that contain more words from the cen- troid of the cluster are considered as central. For- mally, the centroid score of a sentence is the co- sine of the angle between the centroid vector of the whole cluster and the individual centroid of the sen- tence. This is a measure of how close the sentence is to the centroid of the cluster. Centroid-based sum- marization has given promising results in the past (Radev et al., 2001)."
doc2 = "We propose a novel methodology for extractive, generic summarization of text documents. The Maximum Independent Set, which has not been used previously in any summarization study, has been utilized within the context of this study. In addition, a text processing tool, which we named KUSH, is suggested in order to preserve the semantic cohesion between sentences in the representation stage of introductory texts. Our anticipation was that the set of sentences corresponding to the nodes in the inde- pendent set should be excluded from the summary. Based on this anticipation, the nodes forming the Independent Set on the graphs are identified and removed from the graph. Thus, prior to quantification of the effect of the nodes on the global graph, a limitation is applied on the documents to be summarized. This limitation prevents repetition of word groups to be included in the summary. Performance of the proposed approach on the Document Understanding Conference (DUC-2002 and DUC-2004) datasets was calculated using ROUGE evaluation metrics. The developed model achieved a 0.38072 ROUGE perfor- mance value for 100-word summaries, 0.51954 for 200-word summaries, and 0.59208 for 400-word summaries. The values reported throughout the experimental processes of the study reveal the contribu- tion of this innovative method."
text_file_path = "../data/fourier_article.txt"
audio_file_path = "../data/short_fourier_audio.mp3"
# video_file_path = "../data/test_video.mp4"

def summarization():
    sents = nltk.sent_tokenize(doc1)
    # parse document
    # list of dictionary{type='pdf', raw, id}
    print('parsing pdf')
    text_from_document = parse_pdf(text_file_path)
    print(text_from_document[0])

    # parse audio
    # list of dictionary{type='audio', raw, start, end, id}
    print('parsing audio')
    text_from_audio = parse_audio(audio_file_path)
    print(text_from_audio[0])

    #combine the text and audio
    combined_text = text_from_audio + text_from_document
    # print(len(text_from_document), len(text_from_audio))

    print('processing text')
    final_text = preprocessing(combined_text)

    print('summarizing')
    summary = summarize(combined_text)

    #rephrase the sentences
    print('rephrase the sentences')
    final_summary = paraphrase(summary)
    # print(refined_summary)

    for sent in final_summary:
        print(sent['sent'])
        
    return final_summary
    
# file_name = video_file_path.split('_video.mp4')[0]
# audio_file_path = file_name + "_audio.mp3"
    
# audio = video.audio
# audio.write_audiofile(audio_file_path)
    
# print(audio_file_path)
summarization()