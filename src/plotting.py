import matplotlib.pyplot as plt
import pandas as pd
import os

class PlotGraphics:
    def __init__(self):
        pass

    def plot_graphic(self):
        # Criando a figura com 3 subplots (1 linha, 3 colunas)
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        return axes

    def plot_graphic_sex(self, axes, df_sex: pd.DataFrame): 
        # Gráfico 1: Sexo dos passageiros
        axes[0].bar(df_sex['Sex'], df_sex['Count'], color=['blue', 'pink'], alpha=0.7)
        axes[0].set_title('Passengers by Sex', fontsize=14)
        axes[0].set_xlabel('Sex', fontsize=12)
        axes[0].set_ylabel('Count', fontsize=12)
        for i, val in enumerate(df_sex['Count']):
            axes[0].text(i, val + 4, str(val), ha='center', va='bottom', fontsize=10, color='black', weight='bold')
        return axes
    
    def plot_graphic_age(self, axes, age_df: pd.DataFrame):
        # Gráfico 2: Idade dos passageiros
        age_df.plot(kind='bar', ax=axes[1], alpha=0.7)
        axes[1].set_title('Age Distribution by Gender', fontsize=14)
        axes[1].set_xlabel('Age Groups', fontsize=11)
        axes[1].set_ylabel('Count', fontsize=11)
        axes[1].legend(title='Gender')
        axes[1].tick_params(axis='x', rotation=0)
        for bar in axes[1].containers:
            axes[1].bar_label(bar, label_type='edge', fontsize=10, color='black', weight='bold', padding=3)

    def plot_graphic_survivel(self, axes, survivel_rate: pd.DataFrame):
        # Gráfico 3: Taxa de sobrevivência por classe
        axes[2].bar(survivel_rate['Pclass'], survivel_rate['Survival Rate'], color='orange', alpha=0.7)
        axes[2].set_title('Survival Rate by Class', fontsize=14)
        axes[2].set_xlabel('Pclass', fontsize=12)
        axes[2].set_ylabel('Survival Rate', fontsize=12)
        axes[2].set_xticks(survivel_rate['Pclass'])  # Garantir que os ticks do eixo X são as classes
        for i, val in enumerate(survivel_rate['Survival Rate']):
            axes[2].text(i + 1, val + 2, f'{val}', ha='center', va='bottom', fontsize=10, color='black', weight='bold')

    def verify_path(self):
        plt.tight_layout()
        if not os.path.exists("./images"): os.mkdir("./images")

    def save_archive(self, df_sex: pd.DataFrame, age_df: pd.DataFrame, df_survivel: pd.DataFrame):
        axes = self.plot_graphic()
        self.plot_graphic_sex(axes, df_sex)
        self.plot_graphic_age(axes, age_df)
        self.plot_graphic_survivel(axes, df_survivel)
        while True:
            option = input("Do you want save graphic ?(Y/N): ").upper()
            match option:
                case "Y" | "YES":
                    self.verify_path()
                    plt.savefig("./images/Titanic_analysis.png")
                    break
                case "N" | "NO": 
                    plt.show()
                    break
                case _:
                    print("INAVLIDA OPTION")