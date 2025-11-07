// Timestamp: 2025-11-07 01:11:16

export abstract class BaseService {
  protected readonly baseUrl: string;
  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }
}

