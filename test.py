#pip install huggingface_hub requests flask flask-cors

from huggingface_hub import InferenceClient
import os
from typing import Optional
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Mengaktifkan CORS untuk semua route

class PhiClient:
    def __init__(self, api_token: Optional[str] = None):
        """
        Inisialisasi klien Phi-3.5
        :param api_token: Token API Hugging Face (opsional)
        """
        if not api_token:
            raise ValueError("API token diperlukan untuk mengakses model Phi-3.5")
            
        self.repo_id = "microsoft/Phi-3.5-mini-instruct"
        self.client = InferenceClient(
            model=self.repo_id,
            token=api_token
        )

    def generate_text(
        self,
        prompt: str,
        max_new_tokens: int = 200,
        temperature: float = 0.7,
        top_p: float = 0.95,
        repetition_penalty: float = 1.1
    ) -> str:
        """
        Generate teks menggunakan model Phi-3.5
        :param prompt: Input prompt
        :param max_new_tokens: Jumlah maksimum token baru
        :param temperature: Parameter temperature untuk sampling
        :param top_p: Parameter top_p untuk sampling
        :param repetition_penalty: Penalty untuk pengulangan
        :return: Teks yang dihasilkan
        """
        try:
            # Format prompt untuk instruction model
            formatted_prompt = f"Instruct: {prompt}\nOutput:"
            
            # Generate menggunakan text-generation task
            response = self.client.text_generation(
                formatted_prompt,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                repetition_penalty=repetition_penalty,
                return_full_text=False
            )
            return response
            
        except Exception as e:
            raise Exception(f"Error saat generate teks: {str(e)}")

# Inisialisasi PhiClient
api_token = os.getenv("HUGGINGFACE_API_TOKEN")
if not api_token:
    print("Error: HUGGINGFACE_API_TOKEN tidak ditemukan!")
    exit(1)

phi_client = PhiClient(api_token)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Pesan tidak ditemukan'}), 400
            
        message = data['message']
        response = phi_client.generate_text(message)
        return jsonify({'response': response})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Server Flask berjalan di http://localhost:5000")
    app.run(debug=True)