import os
import warnings
import matplotlib.pyplot as plt
import pandas as pd
warnings.filterwarnings("ignore")

class TransformData:
    def __init__(self, directory):
        self.DIRECTORY = directory
        
    
    def get_data_frame(self) -> pd.DataFrame:
        self.df = pd.read_csv(self.DIRECTORY)

        self.df = self.df.dropna(how="all")
        self.df = self.df.drop("PassengerId", axis=1)
        return self.df

    def get_df_survivel(self) -> pd.DataFrame:
        df = self.get_data_frame()
        df_survivel = df[df["Survived"] != 0]
        return df_survivel

    def get_data_sex(self) -> dict:
        df = self.get_data_frame()
        df_survivel = df[df["Survived"] != 0]
        female = len(df_survivel[df_survivel["Sex"].str.contains("female")])
        male = len(df_survivel[df_survivel["Sex"].str.contains("male")])

        

        df_sex = {"Sex":["male","female"],
                "Count":[male,female]
        }
        return df_sex

    def get_data_age(self) -> dict:
        df_survivel = self.get_df_survivel()
        df_survivel["Age"] = df_survivel["Age"].fillna(df_survivel["Age"].mean())
        female_age = df_survivel.loc[df_survivel["Sex"] == "female", "Age"].tolist()
        female_age = pd.Series(female_age)

        male_age = df_survivel.loc[df_survivel["Sex"] == "male", "Age"].tolist()
        male_age = pd.Series(male_age)
        # Define os grupos de idade
        bins = [0, 18, 35, 50, float('inf')]  # Intervalos para os grupos
        labels = ['0-18', '19-35', '36-50', '51+']  # Nomes dos grupos

        # Categoriza as idades em grupos
        male_age_groups = pd.cut(male_age, bins=bins, labels=labels, right=True)
        female_age_groups = pd.cut(female_age, bins=bins, labels=labels, right=True)

        # Conta o número de ocorrências em cada grupo
        male_age_counts = male_age_groups.value_counts(sort=False)
        female_age_counts = female_age_groups.value_counts(sort=False)

        # Exibindo os resultados
        print("Male Age Groups:\n", male_age_counts)
        print("\nFemale Age Groups:\n", female_age_counts)

        #mean age's
        # print(round(female_age.mean()),round(male_age.mean()))

        # print((age.std()/age.mean()) * 100)# to calc standard deviation
        return {"Male":male_age_counts,"Female":female_age_counts}

    def get_social_class(self) -> pd.DataFrame:
        # Calculate survival rate for each class
        df_survivel = self.get_df_survivel()
        survival_rate = df_survivel.groupby("Pclass")["Survived"].sum()
        return survival_rate



# #DataFrames
# td = TransformData(fr"{os.getcwd()}\data\Titanic-Dataset.csv")
# #Get dataframe main
# df = td.get_data_frame()

# #get df_survivel
# df_survivel = td.get_df_survivel()

# #get df_sex and dataframes male's and female's
# df_sex = td.get_data_sex()

# #get df_age and dataframes male's and female's
# df_age = td.get_data_age()
# male_age_counts = df_age["Male"]
# female_age_counts = df_age["Female"]

# survival_rate = td.get_social_class()

# pd.DataFrame(df_sex)#Transform dict age to DataFrame
# age_df = pd.DataFrame({'Male': male_age_counts, 'Female': female_age_counts})
# survivel_rate = pd.DataFrame({'Pclass': survival_rate.index, 'Survival Rate': survival_rate})

# Criando a figura com 3 subplots (1 linha, 3 colunas)
# fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# #region sex
# # Gráfico 1: Sexo dos passageiros
# axes[0].bar(df_sex['Sex'], df_sex['Count'], color=['blue', 'pink'], alpha=0.7)
# axes[0].set_title('Passengers by Sex', fontsize=14)
# axes[0].set_xlabel('Sex', fontsize=12)
# axes[0].set_ylabel('Count', fontsize=12)
# for i, val in enumerate(df_sex['Count']):
#     axes[0].text(i, val + 4, str(val), ha='center', va='bottom', fontsize=10, color='black', weight='bold')
# #endregion

# #region ages
# # Gráfico 2: Idade dos passageiros
# age_df.plot(kind='bar', ax=axes[1], alpha=0.7)
# axes[1].set_title('Age Distribution by Gender', fontsize=14)
# axes[1].set_xlabel('Age Groups', fontsize=11)
# axes[1].set_ylabel('Count', fontsize=11)
# axes[1].legend(title='Gender')
# axes[1].tick_params(axis='x', rotation=0)
# for bar in axes[1].containers:
#     axes[1].bar_label(bar, label_type='edge', fontsize=10, color='black', weight='bold', padding=3)

# #endregion

# #region class of passagers
# # Gráfico 3: Taxa de sobrevivência por classe
# axes[2].bar(survivel_rate['Pclass'], survivel_rate['Survival Rate'], color='orange', alpha=0.7)
# axes[2].set_title('Survival Rate by Class', fontsize=14)
# axes[2].set_xlabel('Pclass', fontsize=12)
# axes[2].set_ylabel('Survival Rate', fontsize=12)
# axes[2].set_xticks(survivel_rate['Pclass'])  # Garantir que os ticks do eixo X são as classes
# for i, val in enumerate(survivel_rate['Survival Rate']):
#     axes[2].text(i + 1, val + 2, f'{val}', ha='center', va='bottom', fontsize=10, color='black', weight='bold')
# #endregion
# # Ajustar o layout para evitar sobreposição
# plt.tight_layout()
# if not os.path.exists("./images"): os.mkdir("./images")
# plt.savefig("./images/Titanic_analysis.png")
# # plt.show()
