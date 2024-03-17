from server.bo.MatchingBO import Matching
from server.db.MatchingMapper import MatchingMapper
from server.Administration.UserProfileAdm import Administration as UserAdm
from server.Administration.SearchProfileAdm import Administration as SearchProfileAdm
from server.Administration.InfoAdm import Administration as InfoAdm
from server.Administration.SelectionAdm import Administration as SelectionAdm
from server.Administration.DescriptionAdm import Administration as DescriptionAdm
from server.Administration.CharacteristicAdm import Administration as CharacteristicAdm
from server.Administration.SimilarityAdm import Administration as SimilarityAdm


class Administration:
    def __init__(self):
        pass

    def get_all_matching(self):
        with MatchingMapper() as mapper:
            return mapper.find_all()

    def get_all_matches_by_userprofile_id(self, userprofile_id):
        with MatchingMapper() as mapper:
            return mapper.find_all_by_userprofile_id(userprofile_id)

    def get_matches_by_userprofile_id(self, userprofile_id):
        with MatchingMapper() as mapper:
            return mapper.find_by_userprofile_id(userprofile_id)

    def matching(self, userprofile_id):
        user_adm = UserAdm()
        potential_profiles = user_adm.get_potential_userprofiles(userprofile_id)
        self.profile_comparison(potential_profiles, userprofile_id)
        self.clean_matches(potential_profiles, self.get_matches_by_userprofile_id(userprofile_id))
        match_list =self.get_matches_by_userprofile_id(userprofile_id)
        return match_list
    
    def profile_comparison(self, potential_profiles, userprofile_id):
        searchprofile_adm = SearchProfileAdm()
        info_adm = InfoAdm()
        selection_adm = SelectionAdm()
        description_adm = DescriptionAdm()
        characteristic_adm = CharacteristicAdm()
        own_searchprofile = searchprofile_adm.get_search_profile_by_userprofile_id(userprofile_id)
        if own_searchprofile is not None:
            own_info_objects = info_adm.get_info_by_searchprofile_id(own_searchprofile.get_id())
            own_question_answer_vector_list = []
            candidate_profile = None
            for info in own_info_objects:
                if info.get_is_selection():
                    answer = selection_adm.get_selection_by_id(info.get_answer_id())
                    characteristic = characteristic_adm.get_characteristic_by_id(answer.get_characteristic_id())
                    own_question_answer_vector = {"question":characteristic, "answer": answer}
                    own_question_answer_vector_list.append(own_question_answer_vector)
                else:
                    answer = description_adm.get_description_by_id(info.get_answer_id())
                    characteristic = characteristic_adm.get_characteristic_by_id(answer.get_characteristic_id()) 
                    own_question_answer_vector = {"question":characteristic, "answer": answer}
                    own_question_answer_vector_list.append(own_question_answer_vector)
            for userprofile in potential_profiles:
                candidate_profile = userprofile.get_id()
                potential_info_objects = info_adm.get_info_by_userprofile_id(userprofile.get_id())
                potential_question_answer_vector_list = []
                for info in potential_info_objects:
                    if info.get_is_selection():
                        answer = selection_adm.get_selection_by_id(info.get_answer_id())
                        characteristic = characteristic_adm.get_characteristic_by_id(answer.get_characteristic_id()) 
                        potential_question_answer_vector = {"question":characteristic, "answer": answer}
                        potential_question_answer_vector_list.append(potential_question_answer_vector)
                    else:
                        answer = description_adm.get_description_by_id(info.get_answer_id())
                        characteristic = characteristic_adm.get_characteristic_by_id(answer.get_characteristic_id()) 
                        potential_question_answer_vector = {"question":characteristic, "answer": answer}
                        potential_question_answer_vector_list.append(potential_question_answer_vector)
                similarity_score = 0
                for vector1 in own_question_answer_vector_list:
                    for vector2 in potential_question_answer_vector_list:
                        if vector1["question"].get_id() == vector2["question"].get_id():
                            if vector1["question"].get_is_selection():
                                if vector1["answer"].get_id() == vector2["answer"].get_id():
                                    similarity_score += 1
                            else:
                                if vector1["answer"].get_answer() != "" and vector2["answer"].get_answer() != "":
                                    if vector1["answer"].get_max_answer() != "":
                                        if vector1["answer"].get_max_answer() == "-":
                                            if int(vector1["answer"].get_answer()) <= int(vector2["answer"].get_answer()):
                                               similarity_score += 1
                                        elif int(vector1["answer"].get_answer()) <= int(vector2["answer"].get_answer()) <= int(vector1["answer"].get_max_answer()):
                                               similarity_score += 1

                                    else:
                                        trimmed_answer1 = self.trim_answer(vector1["answer"].get_answer())
                                        trimmed_answer2 = self.trim_answer(vector2["answer"].get_answer())
                                        print("trimmed_answer1",trimmed_answer1)
                                        print("trimmed_answer2",trimmed_answer2)
                                        is_similar = self.compare_answer(trimmed_answer1, trimmed_answer2)
                                        if is_similar:
                                            similarity_score += 1
                                else:
                                    print("keine antwort")
                relative_similarity = (similarity_score / len(own_question_answer_vector_list)) * 100
                if relative_similarity > 50:
                    self.generate_matching(userprofile_id, candidate_profile, True, relative_similarity)
                    print("MATCH", relative_similarity)
                else:
                    matches = self.get_all_matches_by_userprofile_id(userprofile_id)
                    for match in matches:
                        if((match.get_candidateprofile_id() == candidate_profile) and (match.get_userprofile_id() == userprofile_id)):
                            s_adm = SimilarityAdm()
                            self.delete_matching(match)
                            sim = s_adm.get_similarity_by_matching_id(match.get_id())
                            s_adm.delete_similarity(sim)
                    print("NO MATCH", relative_similarity)
                print("similarity score", similarity_score)
            else:
                print("KEIN SUCHPROFIL")

    def clean_matches(self, potential_match_list, new_match_list):
        sorted_out_matches = []
        s_adm = SimilarityAdm()
        potential_match_ids = [item.get_id() for item in potential_match_list]
        for item in  new_match_list:
            if item.get_candidateprofile_id() not in potential_match_ids:
                sorted_out_matches.append(item)
        for item in sorted_out_matches:
            self.delete_matching(item)
            s_adm.get_similarity_by_matching_id(item.get_id())


    def trim_answer(self, answer):
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        clean_sentence = ''.join(char for char in answer if char not in punctuation)
        split_answer = clean_sentence.lower().split()
        stop_words = ["es", "ist", "auf", "bei", "ob", "wenn", "mir", "dir", "ein",
                      "eines", "einem", "einer", "müssen", "lassen", "damit", "sind",
                       "nur", "wir", "er", "aber", "also", "die", "der", "das", "den"]
        trimmed_answer = [word for word in split_answer if word not in stop_words]
        return trimmed_answer

    def compare_answer(self, answer1, answer2):
        comparison = set(answer1) & set(answer2)
        similarity_score = len(comparison) / len(answer1)
        similar_answer = similarity_score >= 0.7
        return similar_answer

    def get_matching_by_id(self, id):
        with MatchingMapper() as mapper:
            return mapper.find_by_id(id)

    def generate_matching(self, userprofile_id, candidateprofile_id, unseen_profile, similarity_score):
        matching = Matching()
        matching.set_userprofile_id(userprofile_id)
        matching.set_candidateprofile_id(candidateprofile_id)
        matching.set_unseen_profile(unseen_profile)
        matches = self.get_all_matches_by_userprofile_id(userprofile_id)
        s_adm = SimilarityAdm()
        existing_match = False
        existing_object = None
        if len(matches)==0:
            new_match = self.create_matching(userprofile_id, candidateprofile_id, unseen_profile)
            s_adm.create_similarity(new_match.get_id(), similarity_score)
            return new_match
        else:
            for match in matches:
                if((match.get_candidateprofile_id() == candidateprofile_id) and (match.get_userprofile_id() == userprofile_id)):
                    existing_match = True
                    existing_object = match
        if(existing_match is False):
            new_match = self.create_matching(userprofile_id, candidateprofile_id, unseen_profile)
            s_adm.create_similarity(new_match.get_id(), similarity_score)
        else:
            sim_score = s_adm.get_similarity_by_matching_id(existing_object.get_id()) 
            if(round(sim_score.get_score(), 1) == round(similarity_score, 1)):
                return existing_object
            else:
                sim_score.set_score(similarity_score)
                s_adm.update_similarity_by_id(sim_score)
                return existing_object

    def create_matching(self, userprofile_id, candidateprofile_id, unseen_profile):
        matching = Matching()
        matching.set_userprofile_id(userprofile_id)
        matching.set_candidateprofile_id(candidateprofile_id)
        matching.set_unseen_profile(unseen_profile)
        with MatchingMapper() as mapper:
                return mapper.insert(matching)

    def update_matching_by_id(self, matching):
        with MatchingMapper() as mapper:
            return mapper.update_by_id(matching)

    def delete_matching(self, matching):
        with MatchingMapper() as mapper:
            mapper.delete(matching)





